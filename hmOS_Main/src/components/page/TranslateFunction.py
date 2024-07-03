from flask import Flask, request, jsonify
import sys
import time
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import sys
import torch.nn as nn
import torch
import torch.nn.functional as F
from torch.nn import CrossEntropyLoss
import logging
import json
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
import copy
Pprocessor = PythonProcessor()
logger = logging.getLogger(__name__)
import numpy as np
import sys
from config import add_args, set_seed, set_dist
from transformers import (
    RobertaConfig,
    RobertaModel,
    RobertaTokenizer,
    BartConfig,
    BartForConditionalGeneration,
    BartTokenizer,
    T5Config,
    T5ForConditionalGeneration,
    T5Tokenizer
)

import torch.nn as nn

def load_codet5(config, model, tokenizer_class, load_extra_ids=True, add_lang_ids=False,
                tokenizer_path='/export/share/wang.y/workspace/CodeT5Full/tokenizer/salesforce'):
    vocab_fn = '{}/codet5-vocab.json'.format(tokenizer_path)
    merge_fn = '{}/codet5-merges.txt'.format(tokenizer_path)
    tokenizer = tokenizer_class(vocab_fn, merge_fn)

    tokenizer.add_special_tokens(
        {'additional_special_tokens': [
            "<pad>",
            "<s>",
            "</s>",
            "<unk>",
            "<mask>"
        ]})
    if load_extra_ids:
        tokenizer.add_special_tokens(
            {'additional_special_tokens': ['<extra_id_{}>'.format(i) for i in range(99, -1, -1)]})
    if add_lang_ids:
        tokenizer.add_special_tokens({
            'additional_special_tokens': [
                '<en>', '<python>', '<java>', '<javascript>', '<ruby>', '<php>', '<go>', '<c>', '<c_sharp>'
            ]
        })
    # pdb.set_trace()
    tokenizer.model_max_len = 512
    config.num_labels = 1
    config.vocab_size = len(tokenizer)
    config.pad_token_id = 0
    config.bos_token_id = 1
    config.eos_token_id = 2

    model.config = config  # changing the default eos_token_id from 1 to 2
    model.resize_token_embeddings(len(tokenizer))
    return config, model, tokenizer
    
def build_or_load_gen_model(args):
    config_class, model_class, tokenizer_class = MODEL_CLASSES[args.model_type]
    config = config_class.from_pretrained(args.config_name if args.config_name else args.model_name_or_path)
    if args.model_type != 'codet5':
        tokenizer = tokenizer_class.from_pretrained(args.tokenizer_name)
    if args.model_type == 'roberta':
        encoder = model_class.from_pretrained(args.model_name_or_path, config=config)
        decoder_layer = nn.TransformerDecoderLayer(d_model=config.hidden_size, nhead=config.num_attention_heads)
        decoder = nn.TransformerDecoder(decoder_layer, num_layers=6)
        model = Seq2Seq(encoder=encoder, decoder=decoder, config=config,
                        beam_size=args.beam_size, max_length=args.max_target_length,
                        sos_id=tokenizer.cls_token_id, eos_id=tokenizer.sep_token_id)
    else:
        model = model_class.from_pretrained(args.model_name_or_path)

    if args.model_type == 'codet5':
        config, model, tokenizer = load_codet5(config, model, tokenizer_class,
                                               add_lang_ids=args.add_lang_ids,
                                               tokenizer_path=args.tokenizer_path)
    logger.info("Finish loading model [%s] from %s", get_model_size(model), args.model_name_or_path)

    if args.load_model_path is not None:
        logger.info("Reload model from {}".format(args.load_model_path))
        model.load_state_dict(torch.load(args.load_model_path))

    return config, model, tokenizer


class Beam(object):
    def __init__(self, size, sos, eos):
        self.size = size
        self.tt = torch.cuda
        # The score for each translation on the beam.
        self.scores = self.tt.FloatTensor(size).zero_()
        # The backpointers at each time-step.
        self.prevKs = []
        # The outputs at each time-step.
        self.nextYs = [self.tt.LongTensor(size)
                           .fill_(0)]
        self.nextYs[0][0] = sos
        # Has EOS topped the beam yet.
        self._eos = eos
        self.eosTop = False
        # Time and k pair for finished.
        self.finished = []

    def getCurrentState(self):
        "Get the outputs for the current timestep."
        batch = self.tt.LongTensor(self.nextYs[-1]).view(-1, 1)
        return batch

    def getCurrentOrigin(self):
        "Get the backpointers for the current timestep."
        return self.prevKs[-1]

    def advance(self, wordLk):
        """
        Given prob over words for every last beam `wordLk` and attention
        `attnOut`: Compute and update the beam search.

        Parameters:

        * `wordLk`- probs of advancing from the last step (K x words)
        * `attnOut`- attention at the last step

        Returns: True if beam search is complete.
        """
        numWords = wordLk.size(1)

        # Sum the previous scores.
        if len(self.prevKs) > 0:
            beamLk = wordLk + self.scores.unsqueeze(1).expand_as(wordLk)

            # Don't let EOS have children.
            for i in range(self.nextYs[-1].size(0)):
                if self.nextYs[-1][i] == self._eos:
                    beamLk[i] = -1e20
        else:
            beamLk = wordLk[0]
        flatBeamLk = beamLk.view(-1)
        bestScores, bestScoresId = flatBeamLk.topk(self.size, 0, True, True)

        self.scores = bestScores

        # bestScoresId is flattened beam x word array, so calculate which
        # word and beam each score came from
        prevK = bestScoresId // numWords
        self.prevKs.append(prevK)
        self.nextYs.append((bestScoresId - prevK * numWords))

        for i in range(self.nextYs[-1].size(0)):
            if self.nextYs[-1][i] == self._eos:
                s = self.scores[i]
                self.finished.append((s, len(self.nextYs) - 1, i))

        # End condition is when top-of-beam is EOS and no global score.
        if self.nextYs[-1][0] == self._eos:
            self.eosTop = True

    def done(self):
        return self.eosTop and len(self.finished) >= self.size

    def getFinal(self):
        if len(self.finished) == 0:
            self.finished.append((self.scores[0], len(self.nextYs) - 1, 0))
        self.finished.sort(key=lambda a: -a[0])
        if len(self.finished) != self.size:
            unfinished = []
            for i in range(self.nextYs[-1].size(0)):
                if self.nextYs[-1][i] != self._eos:
                    s = self.scores[i]
                    unfinished.append((s, len(self.nextYs) - 1, i))
            unfinished.sort(key=lambda a: -a[0])
            self.finished += unfinished[:self.size - len(self.finished)]
        return self.finished[:self.size]

    def getHyp(self, beam_res):
        """
        Walk back to construct the full hypothesis.
        """
        hyps = []
        for _, timestep, k in beam_res:
            hyp = []
            for j in range(len(self.prevKs[:timestep]) - 1, -1, -1):
                hyp.append(self.nextYs[j + 1][k])
                k = self.prevKs[j][k]
            hyps.append(hyp[::-1])
        return hyps

    def buildTargetTokens(self, preds):
        sentence = []
        for pred in preds:
            tokens = []
            for tok in pred:
                if tok == self._eos:
                    break
                tokens.append(tok)
            sentence.append(tokens)
        return sentence

class Seq2Seq(nn.Module):
    """
        Build Seqence-to-Sequence.

        Parameters:

        * `encoder`- encoder of seq2seq model. e.g. roberta
        * `decoder`- decoder of seq2seq model. e.g. transformer
        * `config`- configuration of encoder model.
        * `beam_size`- beam size for beam search.
        * `max_length`- max length of target for beam search.
        * `sos_id`- start of symbol ids in target for beam search.
        * `eos_id`- end of symbol ids in target for beam search.
    """

    def __init__(self, encoder, decoder, config, beam_size=None, max_length=None, sos_id=None, eos_id=None):
        super(Seq2Seq, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.config = config
        self.register_buffer("bias", torch.tril(torch.ones(2048, 2048)))
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        self.lm_head = nn.Linear(config.hidden_size, config.vocab_size, bias=False)
        self.lsm = nn.LogSoftmax(dim=-1)
        self.tie_weights()

        self.beam_size = beam_size
        self.max_length = max_length
        self.sos_id = sos_id
        self.eos_id = eos_id

    def _tie_or_clone_weights(self, first_module, second_module):
        """ Tie or clone module weights depending of weither we are using TorchScript or not
        """
        if self.config.torchscript:
            first_module.weight = nn.Parameter(second_module.weight.clone())
        else:
            first_module.weight = second_module.weight

    def tie_weights(self):
        """ Make sure we are sharing the input and output embeddings.
            Export to TorchScript can't handle parameter sharing so we are cloning them instead.
        """
        self._tie_or_clone_weights(self.lm_head,
                                   self.encoder.embeddings.word_embeddings)

    def forward(self, source_ids=None, source_mask=None, target_ids=None, target_mask=None, args=None):
        outputs = self.encoder(source_ids, attention_mask=source_mask)
        encoder_output = outputs[0].permute([1, 0, 2]).contiguous()
        if target_ids is not None:
            attn_mask = -1e4 * (1 - self.bias[:target_ids.shape[1], :target_ids.shape[1]])
            tgt_embeddings = self.encoder.embeddings(target_ids).permute([1, 0, 2]).contiguous()
            out = self.decoder(tgt_embeddings, encoder_output, tgt_mask=attn_mask,
                               memory_key_padding_mask=~source_mask)
            # memory_key_padding_mask=(1 - source_mask).bool())
            hidden_states = torch.tanh(self.dense(out)).permute([1, 0, 2]).contiguous()
            lm_logits = self.lm_head(hidden_states)
            # Shift so that tokens < n predict n
            active_loss = target_mask[..., 1:].ne(0).view(-1) == 1
            shift_logits = lm_logits[..., :-1, :].contiguous()
            shift_labels = target_ids[..., 1:].contiguous()
            # Flatten the tokens
            loss_fct = nn.CrossEntropyLoss(ignore_index=-1)
            loss = loss_fct(shift_logits.view(-1, shift_logits.size(-1))[active_loss],
                            shift_labels.view(-1)[active_loss])

            outputs = loss, loss * active_loss.sum(), active_loss.sum()
            return outputs
        else:
            # Predict
            preds = []
            zero = torch.cuda.LongTensor(1).fill_(0)
            for i in range(source_ids.shape[0]):
                context = encoder_output[:, i:i + 1]
                context_mask = source_mask[i:i + 1, :]
                beam = Beam(self.beam_size, self.sos_id, self.eos_id)
                input_ids = beam.getCurrentState()
                context = context.repeat(1, self.beam_size, 1)
                context_mask = context_mask.repeat(self.beam_size, 1)
                for _ in range(self.max_length):
                    if beam.done():
                        break
                    attn_mask = -1e4 * (1 - self.bias[:input_ids.shape[1], :input_ids.shape[1]])
                    tgt_embeddings = self.encoder.embeddings(input_ids).permute([1, 0, 2]).contiguous()
                    out = self.decoder(tgt_embeddings, context, tgt_mask=attn_mask,
                                       memory_key_padding_mask=~context_mask)
                    # memory_key_padding_mask=(1 - context_mask).bool())
                    out = torch.tanh(self.dense(out))
                    hidden_states = out.permute([1, 0, 2]).contiguous()[:, -1, :]
                    out = self.lsm(self.lm_head(hidden_states)).data
                    beam.advance(out)
                    input_ids.data.copy_(input_ids.data.index_select(0, beam.getCurrentOrigin()))
                    input_ids = torch.cat((input_ids, beam.getCurrentState()), -1)
                hyp = beam.getHyp(beam.getFinal())
                pred = beam.buildTargetTokens(hyp)[:self.beam_size]
                pred = [torch.cat([x.view(-1) for x in p] + [zero] * (self.max_length - len(p))).view(1, -1) for p in
                        pred]
                preds.append(torch.cat(pred, 0).unsqueeze(0))

            preds = torch.cat(preds, 0)
            return preds

MODEL_CLASSES = {'roberta': (RobertaConfig, RobertaModel, RobertaTokenizer),
                 't5': (T5Config, T5ForConditionalGeneration, T5Tokenizer),
                 'codet5': (T5Config, T5ForConditionalGeneration, RobertaTokenizer),
                 'bart': (BartConfig, BartForConditionalGeneration, BartTokenizer)}



import argparse

def get_model_size(model):
    model_parameters = filter(lambda p: p.requires_grad, model.parameters())
    model_size = sum([np.prod(p.size()) for p in model_parameters])
    return "{}M".format(round(model_size / 1e+6))
class hmCodeTrans:  # 定义类
    def __init__(self):
        self.GTM, self.GTM_tokenizer = self.get_GTM_model()
        
        self.ml_classifier_dic = self.bulid_ml_classifier()
        
        logger.info("hmCodeTrans initialization successful!")
        self.attention_cache_dic = dict()  # 存放会话中用户的Attention Cache信息
        self.sequence_outputs_dic = dict()  # 存放后缀拼接信息
        self.first_output_dic = dict()  # 存放first_output信息
        self.token_dic_dic = dict()  # 存放token_dic
        self.immediate_result_dic = dict()  # 存放会话用户的中间结果信息
        self.java_data = self.read_data_from_java_file()
        self.python_data = self.read_data_from_python_file()
        self.cound_id = 0


    def bulid_ml_classifier(self):
        import pickle
        with open(r".\src\classifier\adaboost.pickle", 'rb') as f:
            adboost = pickle.load(f)
        with open(r".\src\classifier\svm.pickle", 'rb') as f:
            svm = pickle.load(f)
        with open(r".\src\classifier\gbdt.pickle", 'rb') as f:
            gdbt = pickle.load(f)
        with open(r".\src\classifier\j2p_adaboost.pickle", 'rb') as f:
            j2p_adboost = pickle.load(f)
        with open(r".\src\classifier\j2p_gbdt.pickle", 'rb') as f:
            j2p_svm = pickle.load(f)
        with open(r".\src\classifier\j2p_svm.pickle", 'rb') as f:
            j2p_gdbt = pickle.load(f)
        return {'p2j': [svm, gdbt, adboost], 'j2p': [j2p_svm, j2p_gdbt, j2p_adboost]}

   

    def get_GTM_model(self):
        sys.argv = [r'.\src\components\page\run_gen.py',
                    '--do_test',
                    '--model_type', 'codet5',
                    '--tokenizer_name', 'roberta-base',
                    '--tokenizer_path', r'E:/code/UI/AVATAR-main/codet5/bpe',
                    '--model_name_or_path', r'E:/code/UI/AVATAR-main/codet5/codet5_base',
                    '--task', 'translate',
                    '--sub_task', 'python-java',
                    '--output_dir', 'E:\\code\\UI\\AVATAR-main\\codet5\\g4g\\python2java\\in_segment\\transcoder_eval',
                    '--data_dir', '.E:/code/UI/AVATAR-main/codet5/\data\\transcoder_test_gfg',
                    '--cache_path',
                    'E:\\code\\UI\\AVATAR-main\\codet5\\g4g\\python2java\\in_segment\\transcoder_eval\\cached_data',
                    '--res_dir', '.g4g\\python2java\\in_segment\\transcoder_eval',
                    '--eval_batch_size', '1',
                    '--max_source_length', '510',
                    '--max_target_length', '510',
                    '--beam_size', '1',
                    '--trained_model_path',
                    r'.\src\GTM_model\pytorch_model_gtm.bin']
        parser = argparse.ArgumentParser()
        args = add_args(parser)
        logger.info(args)
        set_dist(args)
        set_seed(args)
        config, model, tokenizer = build_or_load_gen_model(args)
        model.to(args.device)
        model.load_state_dict(torch.load(args.trained_model_path))
        return model, tokenizer


    def deal_with_one_kuohao(self, prefix):
        for i in range(len(prefix) - 1, -1, -1):
            if prefix[i] == ')':
                return prefix, ''
            elif prefix[i] == '(':
                return prefix[:i], prefix[i:]
        return prefix, ''

    def traverse_list(self, prefix_token_before_zuokuohao):
        for i in range(len(prefix_token_before_zuokuohao) - 1, -1, -1):
            if prefix_token_before_zuokuohao[i] in ['NEW_LINE', 'DEDENT', 'INDENT']:
                prefix_token_before_zuokuohao.pop(i)
            else:
                return prefix_token_before_zuokuohao

    def get_res_by_pc_based_hmCodeTrans(self, src, prefix, session_id, translate_direction='p2j'):
        # global machine_time
        logger.info("receive the msg {} from session:{}".format(str({'source program: ': src, 'prefix: ': prefix}),
                                                                str(session_id)))
        if translate_direction[0] == 'p':
            src = ' '.join(Pprocessor.tokenize_code(src.strip()))
        if translate_direction[-1] == 'p' and prefix != "":
            last_token = prefix.split(" ")[-1]
            prefix_before_zuokuohao, prefix_after_zuokuohao = self.deal_with_one_kuohao(prefix)
            prefix_token_before_zuokuohao = self.traverse_list(Pprocessor.tokenize_code(
                prefix_before_zuokuohao.strip())) if prefix_after_zuokuohao != '' else Pprocessor.tokenize_code(
                prefix_before_zuokuohao.strip())
            last_token_index = 0 if prefix_after_zuokuohao == '' else len(prefix_token_before_zuokuohao)
            if prefix_after_zuokuohao == '':
                for index in range(len(prefix_token_before_zuokuohao) - 1, -1, -1):
                    if prefix_token_before_zuokuohao[index] == last_token:
                        last_token_index = index
                        break
            prefix_temp = ' '.join(prefix_token_before_zuokuohao[:last_token_index + 1])
            prefix = prefix_temp + ' ' + prefix_after_zuokuohao if prefix_after_zuokuohao != '' else prefix_temp
        if session_id not in self.immediate_result_dic:
            start_time = time.time()
            res, length = self.get_first_res_by_GTM(src, session_id, translate_direction)
            end_time = time.time()
            # machine_time.append(end_time - start_time)
        else:
            start_time = time.time()
            res, length = self.get_res_by_GTM(src, prefix, session_id, translate_direction)
            end_time = time.time()

            # machine_time.append(end_time-start_time)
            # print(machine_time)
        return Pprocessor.detokenize_code(res.strip()) if translate_direction[-1] == 'p' else res, length

    
    def read_from_file(self, file_name):
        with open(file_name) as f:
            return json.loads(f.read())

    def read_data_from_java_file(self):
        data = [
                'static void printSubstrings ( int n ) { int s = ( int ) Math . log10 ( n ) ; int d = ( int ) ( Math . pow ( 10 , s ) + 0.5 ) ; int k = d ; while ( n > 0 ) { while ( d > 0 ) { System . out . println ( n / d ) ; d = d / 10 ; } n = n % k ; k = k / 10 ; d = k ; } }',
                'static int minSteps ( int i , int j , int arr [ ] [ ] ) { if ( i == n - 1 && j == n - 1 ) { return 0 ; } if ( i > n - 1 || j > n - 1 ) { return 9999999 ; } if ( v [ i ] [ j ] == 1 ) { return dp [ i ] [ j ] ; } v [ i ] [ j ] = 1 ; dp [ i ] [ j ] = 1 + Math . min ( minSteps ( i + arr [ i ] [ j ] , j , arr ) , minSteps ( i , j + arr [ i ] [ j ] , arr ) ) ; return dp [ i ] [ j ] ; }',
                'static int maxDiff ( int [ ] arr , int n ) { int SubsetSum_1 = 0 , SubsetSum_2 = 0 ; for ( int i = 0 ; i <= n - 1 ; i ++ ) { boolean isSingleOccurance = true ; for ( int j = i + 1 ; j <= n - 1 ; j ++ ) { if ( arr [ i ] == arr [ j ] ) { isSingleOccurance = false ; arr [ i ] = arr [ j ] = 0 ; break ; } } if ( isSingleOccurance ) { if ( arr [ i ] > 0 ) SubsetSum_1 += arr [ i ] ; else SubsetSum_2 += arr [ i ] ; } } return Math . abs ( SubsetSum_1 - SubsetSum_2 ) ; }',
                'static int countConsecutive ( int n ) { String s = Integer . toString ( n ) ; int count = 0 ; for ( int i = 0 ; i < s . length ( ) - 1 ; i ++ ) if ( s . charAt ( i ) == s . charAt ( i + 1 ) ) count ++ ; return count ; }',
                'static int productDiagonals ( int arr [ ] [ ] , int n ) { int product = 1 ; for ( int i = 0 ; i < n ; i ++ ) { product = product * arr [ i ] [ i ] ; product = product * arr [ i ] [ n - i - 1 ] ; } if ( n % 2 == 1 ) { product = product / arr [ n / 2 ] [ n / 2 ] ; } return product ; }'
                'static int longestSubarry ( int arr [ ] , int n ) { int res = 0 ; for ( int i = 0 ; i < n ; i ++ ) { int curr_count = 0 ; while ( i < n && arr [ i ] >= 0 ) { curr_count ++ ; i ++ ; } res = Math . max ( res , curr_count ) ; } return res ; }',
                'static int oddFib ( int n ) { n = ( 3 * n + 1 ) / 2 ; int a = - 1 , b = 1 , c = 0 , i ; for ( i = 1 ; i <= n ; i ++ ) { c = a + b ; a = b ; b = c ; } return c ; }',
                'static int seriesSum ( int calculated , int current , int N ) { int i , cur = 1 ; if ( current == N + 1 ) return 0 ; for ( i = calculated ; i < calculated + current ; i ++ ) cur *= i ; return cur + seriesSum ( i , current + 1 , N ) ; }',
                'static int countSegments ( int a [ ] , int n , int x ) { boolean flag = false ; int count = 0 ; for ( int i = 0 ; i < n ; i ++ ) { if ( a [ i ] > x ) { flag = true ; } else { if ( flag ) count += 1 ; flag = false ; } } return count ; }',
                'static void merge ( int m , int n ) { for ( int i = n - 1 ; i >= 0 ; i -- ) { int j , last = arr1 [ m - 1 ] ; for ( j = m - 2 ; j >= 0 && arr1 [ j ] > arr2 [ i ] ; j -- ) arr1 [ j + 1 ] = arr1 [ j ] ; if ( j != m - 2 || last > arr2 [ i ] ) { arr1 [ j + 1 ] = arr2 [ i ] ; arr2 [ i ] = last ; } } }'
                ]
       
        return data

    def read_data_from_python_file(self):
        data = [
            'def longestSubarry ( arr , n ) : NEW_LINE INDENT res = 0 NEW_LINE for i in range ( n ) : NEW_LINE INDENT curr_count = 0 NEW_LINE while ( i < n and arr [ i ] >= 0 ) : NEW_LINE INDENT curr_count += 1 NEW_LINE i += 1 NEW_LINE DEDENT res = max ( res , curr_count ) NEW_LINE DEDENT return res NEW_LINE DEDENT',
            'def closestNumber ( n , m ) : NEW_LINE INDENT q = int ( n / m ) NEW_LINE n1 = m * q NEW_LINE if ( ( n * m ) > 0 ) : NEW_LINE INDENT n2 = ( m * ( q + 1 ) ) NEW_LINE DEDENT else : NEW_LINE INDENT n2 = ( m * ( q - 1 ) ) NEW_LINE DEDENT if ( abs ( n - n1 ) < abs ( n - n2 ) ) : NEW_LINE INDENT return n1 NEW_LINE DEDENT return n2 NEW_LINE DEDENT',
            'def maxAND ( L , R ) : NEW_LINE INDENT maximum = L & R NEW_LINE for i in range ( L , R , 1 ) : NEW_LINE INDENT for j in range ( i + 1 , R + 1 , 1 ) : NEW_LINE INDENT maximum = max ( maximum , ( i & j ) ) NEW_LINE DEDENT DEDENT return maximum NEW_LINE DEDENT',
            'def printSubstrings ( n ) : NEW_LINE INDENT s = int ( math . log10 ( n ) ) ; NEW_LINE d = ( math . pow ( 10 , s ) ) ; NEW_LINE k = d ; NEW_LINE while ( n > 0 ) : NEW_LINE INDENT while ( d > 0 ) : NEW_LINE INDENT print ( int ( n // d ) ) ; NEW_LINE d = int ( d / 10 ) ; NEW_LINE DEDENT n = int ( n % k ) ; NEW_LINE k = int ( k // 10 ) ; NEW_LINE d = k ; NEW_LINE DEDENT DEDENT',
                'def minsteps ( n , m ) : NEW_LINE INDENT if ( m > n ) : NEW_LINE INDENT return - 1 NEW_LINE DEDENT else : NEW_LINE INDENT return ( ( n + 1 ) // 2 + m - 1 ) // m * m  NEW_LINE DEDENT DEDENT',
                'def totalSumDivisibleByNum ( digit , number ) : NEW_LINE INDENT firstnum = pow ( 10 , digit - 1 ) NEW_LINE lastnum = pow ( 10 , digit ) NEW_LINE firstnum = ( firstnum - firstnum % number ) + number NEW_LINE lastnum = ( lastnum - lastnum % number ) NEW_LINE count = ( ( lastnum - firstnum ) / number + 1 ) NEW_LINE return int ( ( ( lastnum + firstnum ) * count ) / 2 ) NEW_LINE DEDENT',
                'def oddFib ( n ) : NEW_LINE INDENT n = ( 3 * n + 1 ) // 2 NEW_LINE a = - 1 NEW_LINE b = 1 NEW_LINE c = 0 NEW_LINE for i in range ( 1 , n + 1 ) : NEW_LINE INDENT c = a + b NEW_LINE a = b NEW_LINE b = c NEW_LINE DEDENT return c NEW_LINE DEDENT',
                'def seriesSum ( calculated , current , N ) : NEW_LINE INDENT i = calculated ; NEW_LINE cur = 1 ; NEW_LINE if ( current == N + 1 ) : NEW_LINE INDENT return 0 ; NEW_LINE DEDENT while ( i < calculated + current ) : NEW_LINE INDENT cur *= i ; NEW_LINE i += 1 ; NEW_LINE DEDENT return cur + seriesSum ( i , current + 1 , N ) ; NEW_LINE DEDENT',
                'def CountSegments ( N , a ) : NEW_LINE INDENT frequency = [ 0 ] * 10001 NEW_LINE c = 0 NEW_LINE for i in range ( N ) : NEW_LINE INDENT frequency [ a [ i ] ] += 1 NEW_LINE DEDENT for i in range ( 10001 ) : NEW_LINE INDENT c = max ( c , frequency [ i ] ) NEW_LINE DEDENT print ( c ) NEW_LINE DEDENT',
                'def merge ( ar1 , ar2 , m , n ) : NEW_LINE INDENT for i in range ( n - 1 , - 1 , - 1 ) : NEW_LINE INDENT last = ar1 [ m - 1 ] NEW_LINE j = m - 2 NEW_LINE while ( j >= 0 and ar1 [ j ] > ar2 [ i ] ) : NEW_LINE INDENT ar1 [ j + 1 ] = ar1 [ j ] NEW_LINE j -= 1 NEW_LINE DEDENT if ( j != m - 2 or last > ar2 [ i ] ) : NEW_LINE INDENT ar1 [ j + 1 ] = ar2 [ i ] NEW_LINE ar2 [ i ] = last NEW_LINE DEDENT DEDENT DEDENT',
                ]
           
        return data
    
    def write_file(self, file_path, data):
        with open(file_path, 'a') as f:
            f.write(json.dumps(data))
            f.close()

    

    def get_first_res_by_GTM(self, src, session_id, translate_direction='p2j'):
        source_ids = self.GTM_tokenizer.encode(src.strip())
        source_ids.extend([0] * (510 - len(source_ids)))
        source_ids = torch.tensor([source_ids], device='cuda:0')
        source_mask = source_ids.ne(self.GTM_tokenizer.pad_token_id)
        start = time.time()
        logger.info("hmCodeTrans is translating...")
        model = self.GTM if translate_direction == 'p2j' else self.j2p_GTM
        preds, past, sequence_outputs, first_output = model.generate(source_ids,
                                                                     attention_mask=source_mask,
                                                                     use_cache=True,
                                                                     num_beams=1,
                                                                     early_stopping=False,
                                                                     max_length=510,
                                                                     num_return_sequences=1,
                                                                     prefix=[0],
                                                                     prefix_len=1,
                                                                     # 用户真实验证的前缀长度
                                                                     tokenizer=self.GTM_tokenizer,
                                                                     least_past=None,
                                                                     # 实际的某个局部状态，小于等于 前缀长度-1
                                                                     is_past=True,
                                                                     is_concent_sufix=True,
                                                                     token_dic=None,
                                                                     greedy_mode=False,
                                                                     dic_prefix={},
                                                                     pattern=2,
                                                                     classfier=2,
                                                                     classifier_list=self.ml_classifier_dic[
                                                                         translate_direction]
                                                                     )
        end = time.time()
        logger.info('It took {} seconds to translate the program'.format(round(end - start, 2)))
        im = list(preds[0][1:].cpu().numpy())[1:-1]
        token_dic = {}
        for c, (token, sequence_output) in enumerate(zip(first_output, sequence_outputs)):
            if token not in token_dic.keys():
                token_dic[token] = [(c, sequence_output)]
            else:
                token_dic[token].append((c, sequence_output))
        self.immediate_result_dic[session_id] = [im]
        self.attention_cache_dic[session_id] = past
        self.sequence_outputs_dic[session_id] = sequence_outputs
        self.token_dic_dic[session_id] = token_dic
        self.first_output_dic[session_id] = first_output
        return self.GTM_tokenizer.decode(im), len(im)

    def get_res_by_GTM(self, src, prefix, session_id, translate_direction='p2j'):
        source_ids = self.GTM_tokenizer.encode(src.strip())
        source_ids.extend([0] * (510 - len(source_ids)))
        source_ids = torch.tensor([source_ids], device='cuda:0')
        source_mask = source_ids.ne(self.GTM_tokenizer.pad_token_id)
        prefix = self.GTM_tokenizer.encode(prefix.strip())[:-1]
        tgt_len = len(prefix) - 1
        past = self.attention_cache_dic[session_id]
        if past[1] is not None:
            res_tuple = []
            for i in past[1]:
                cur_tuple = []
                for index, j in enumerate(i):
                    if index in [0, 1]:
                        cur_tuple.append(j[:, :, :min(tgt_len + 1, j.shape[2]), :])  # 可能状态的值小于前缀的长度-1
                    else:
                        cur_tuple.append(j)
                res_tuple.append(tuple(cur_tuple))
            past = tuple([past[0], tuple(res_tuple)])
        start = time.time()
        logger.info("hmCodeTrans is translating...")
        model = self.GTM if translate_direction == 'p2j' else self.j2p_GTM
        preds, past, best_suffix, has_contains_false = model.generate(source_ids,
                                                                      attention_mask=source_mask,
                                                                      use_cache=True,
                                                                      num_beams=1,
                                                                      early_stopping=False,
                                                                      max_length=510,
                                                                      num_return_sequences=1,
                                                                      prefix=prefix,
                                                                      prefix_len=len(prefix),
                                                                      # 用户真实验证的前缀长度
                                                                      tokenizer=self.GTM_tokenizer,
                                                                      least_past=past,
                                                                      # 实际的某个局部状态，小于等于 前缀长度-1
                                                                      is_past=True,
                                                                      is_concent_sufix=True,
                                                                      sequence_outputs=self.sequence_outputs_dic[
                                                                          session_id],
                                                                      first_output=self.first_output_dic[session_id],
                                                                      token_dic=self.token_dic_dic[session_id],
                                                                      greedy_mode=False,
                                                                      dic_prefix={},
                                                                      pattern=2,
                                                                      classfier=2,
                                                                      classifier_list=self.ml_classifier_dic[
                                                                          translate_direction]
                                                                      )
        end = time.time()
        logger.info('It took {} seconds to translate the program'.format(round(end - start, 2)))
        im = list(preds[0][1:].cpu().numpy())[1:-1]
        self.immediate_result_dic[session_id].append(im)
        self.attention_cache_dic[session_id] = past
        return self.GTM_tokenizer.decode(im), len(im)

    