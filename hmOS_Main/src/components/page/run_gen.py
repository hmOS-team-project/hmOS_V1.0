# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Fine-tuning the library models for language modeling on a text file (GPT, GPT-2, BERT, RoBERTa).
GPT and GPT-2 are fine-tuned using a causal language modeling (CLM) loss while BERT and RoBERTa are fine-tuned
using a masked language modeling (MLM) loss.
"""
from torch.utils.data import TensorDataset
# import numpy as np
# import logging
# import os
import torch.nn as nn
import random
# import torch
import time
# from tqdm import tqdm
import os
import torch
import logging
import argparse
import math
import numpy as np
from tqdm import tqdm
import multiprocessing
import time
import sys
import pdb
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader, SequentialSampler, RandomSampler
from torch.utils.data.distributed import DistributedSampler
# sys.path.append('..')
from TransModels import build_or_load_gen_model
from TransModels import get_filenames, get_elapse_time, load_and_cache_gen_data
from config import add_args, set_seed, set_dist
from transformers import AdamW, get_linear_schedule_with_warmup
import smooth_bleu
from bleu import _bleu
# from CodeBLEU import calc_code_bleu

def get_elapse_time(t0):
    elapse_time = time.time() - t0
    if elapse_time > 3600:
        hour = int(elapse_time // 3600)
        minute = int((elapse_time % 3600) // 60)
        return "{}h{}m".format(hour, minute)
    else:
        minute = int((elapse_time % 3600) // 60)
        return "{}m".format(minute)

# def load_and_cache_gen_data(args, filename, pool, tokenizer, split_tag, only_src=False, is_sample=False):
#     # cache the data into args.cache_path except it is sampled
#     # only_src: control whether to return only source ids for bleu evaluating (dev\\test)
#     # return: examples (Example object), data (TensorDataset)
#     data_tag = '_all' if args.data_num == -1 else '_%d' % args.data_num
#     cache_fn = '{}\\{}.pt'.format(args.cache_path, split_tag + ('_src' if only_src else '') + data_tag)

#     examples = read_examples(filename, args.data_num, args.task)

#     if is_sample:
#         examples = random.sample(examples, min(5000, len(examples)))
#     if split_tag == 'train':
#         calc_stats(examples, tokenizer, is_tokenize=True)
#     else:
#         calc_stats(examples)
#     if False:
#         logger.info("Load cache data from %s", cache_fn)
#         data = torch.load(cache_fn)
#     else:
#         if is_sample:
#             logger.info("Sample 5k data for computing bleu from %s", filename)
#         else:
#             logger.info("Create cache data into %s", cache_fn)
#         tuple_examples = [(example, idx, tokenizer, args, split_tag) for idx, example in enumerate(examples)]
#         features = pool.map(convert_examples_to_features, tqdm(tuple_examples, total=len(tuple_examples)))
#         all_source_ids = torch.tensor([f.source_ids for f in features], dtype=torch.long)
#         #----------
#         templ = [[32049] * 1 for _ in range(0, all_source_ids.shape[0])]
#         tempt = torch.tensor(templ)
#         all_source_ids_2 = torch.cat((tempt, all_source_ids), 1)
#         all_source_ids_2 = torch.split(all_source_ids_2, [510, 1], 1)[0]
#         all_source_ids_3 = torch.cat((all_source_ids, all_source_ids_2), 0)
#         #----------
#         if split_tag == 'test' or only_src:
#             data = TensorDataset(all_source_ids)
#         else:
#             all_target_ids = torch.tensor([f.target_ids for f in features], dtype=torch.long)
#             import copy
#             all_target_ids_2 = copy.deepcopy(all_target_ids)
#             for i in range(0, all_target_ids.shape[0]):
#                 for j in range(0, all_target_ids.shape[1]):
#                     if all_target_ids[i][j] == 2:
#                         for m in range(1, int((j + 1) / 2)):
#                             temp = int(all_target_ids[i][m])
#                             all_target_ids[i][m] = all_target_ids[i][j - m];
#                             all_target_ids[i][j - m] = temp;
#             all_target_ids_3 = torch.cat((all_target_ids_2, all_target_ids), 0)


#             data = TensorDataset(all_source_ids_3, all_target_ids_3)
#         if args.local_rank in [-1, 0] and not is_sample:
#             torch.save(data, cache_fn)
#     return examples, data


def get_filenames(data_root, task, sub_task, split=''):
    if task == 'concode':
        data_dir = '{}\\{}'.format(data_root, task)
        train_fn = '{}\\train.json'.format(data_dir)
        dev_fn = '{}\\dev.json'.format(data_dir)
        test_fn = '{}\\test.json'.format(data_dir)
    elif task == 'summarize':
        data_dir = '{}\\{}\\{}'.format(data_root, task, sub_task)
        train_fn = '{}\\train.jsonl'.format(data_dir)
        dev_fn = '{}\\valid.jsonl'.format(data_dir)
        test_fn = '{}\\test.jsonl'.format(data_dir)
    elif task == 'refine':
        data_dir = '{}\\{}\\{}'.format(data_root, task, sub_task)
        train_fn = '{}\\train.buggy-fixed.buggy,{}\\train.buggy-fixed.fixed'.format(data_dir, data_dir)
        dev_fn = '{}\\valid.buggy-fixed.buggy,{}\\valid.buggy-fixed.fixed'.format(data_dir, data_dir)
        test_fn = '{}\\test.buggy-fixed.buggy,{}\\test.buggy-fixed.fixed'.format(data_dir, data_dir)
    elif task == 'translate':
        if sub_task in ['java-python', 'python-java']:
            src, tgt = sub_task.split('-')
            train_fn = '{}\\train.java-python.{},{}\\train.java-python.{}'.format(data_root, src, data_root, tgt)
            dev_fn = '{}\\valid.java-python.{},{}\\valid.java-python.{}'.format(data_root, src, data_root, tgt)
            test_fn = '{}\\test.java-python.{},{}\\test.java-python.{}'.format(data_root, src, data_root, tgt)
        else:
            data_dir = '{}\\{}'.format(data_root, task)
            if sub_task == 'cs-java':
                train_fn = '{}\\train.java-cs.txt.cs,{}\\train.java-cs.txt.java'.format(data_dir, data_dir)
                dev_fn = '{}\\valid.java-cs.txt.cs,{}\\valid.java-cs.txt.java'.format(data_dir, data_dir)
                test_fn = '{}\\test.java-cs.txt.cs,{}\\test.java-cs.txt.java'.format(data_dir, data_dir)
            else:
                train_fn = '{}\\train.java-cs.txt.java,{}\\train.java-cs.txt.cs'.format(data_dir, data_dir)
                dev_fn = '{}\\valid.java-cs.txt.java,{}\\valid.java-cs.txt.cs'.format(data_dir, data_dir)
                test_fn = '{}\\test.java-cs.txt.java,{}\\test.java-cs.txt.cs'.format(data_dir, data_dir)
    elif task == 'clone':
        data_dir = '{}\\{}'.format(data_root, task)
        train_fn = '{}\\train.txt'.format(data_dir)
        dev_fn = '{}\\valid.txt'.format(data_dir)
        test_fn = '{}\\test.txt'.format(data_dir)
    elif task == 'defect':
        data_dir = '{}\\{}'.format(data_root, task)
        train_fn = '{}\\train.jsonl'.format(data_dir)
        dev_fn = '{}\\valid.jsonl'.format(data_dir)
        test_fn = '{}\\test.jsonl'.format(data_dir)
    if split == 'train':
        return train_fn
    elif split == 'dev':
        return dev_fn
    elif split == 'test':
        return test_fn
    else:
        return train_fn, dev_fn, test_fn

# def build_or_load_gen_model(args):
#     config_class, model_class, tokenizer_class = MODEL_CLASSES[args.model_type]
#     config = config_class.from_pretrained(args.config_name if args.config_name else args.model_name_or_path)
#     if args.model_type != 'codet5':
#         tokenizer = tokenizer_class.from_pretrained(args.tokenizer_name)
#     if args.model_type == 'roberta':
#         encoder = model_class.from_pretrained(args.model_name_or_path, config=config)
#         decoder_layer = nn.TransformerDecoderLayer(d_model=config.hidden_size, nhead=config.num_attention_heads)
#         decoder = nn.TransformerDecoder(decoder_layer, num_layers=6)
#         model = Seq2Seq(encoder=encoder, decoder=decoder, config=config,
#                         beam_size=args.beam_size, max_length=args.max_target_length,
#                         sos_id=tokenizer.cls_token_id, eos_id=tokenizer.sep_token_id)
#     else:
#         model = model_class.from_pretrained(args.model_name_or_path)

#     if args.model_type == 'codet5':
#         # reset special ids: pad_token_id = 0, bos_token_id = 1, eos_token_id = 2
#         config, model, tokenizer = load_codet5(config, model, tokenizer_class,
#                                                add_lang_ids=args.add_lang_ids,
#                                                tokenizer_path=args.tokenizer_path)
#     logger.info("Finish loading model [%s] from %s", get_model_size(model), args.model_name_or_path)

#     if args.load_model_path is not None:
#         logger.info("Reload model from {}".format(args.load_model_path))
#         model.load_state_dict(torch.load(args.load_model_path))

#     return config, model, tokenizer

# logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S',
#                     level=logging.INFO)
# logger = logging.getLogger(__name__)


# def (args, eval_data, eval_examples, model, tokenizer):
#     eval_sampler = SequentialSampler(eval_data)
#     eval_dataloader = DataLoader(eval_data, sampler=eval_sampler, batch_size=args.eval_batch_size,
#                                  num_workers=4, pin_memory=True)
#     # Start evaluating model
#     logger.info(eval_ppl_epoch"  " + "***** Running ppl evaluation *****")
#     logger.info("  Num examples = %d", len(eval_examples))
#     logger.info("  Batch size = %d", args.eval_batch_size)

#     model.eval()
#     eval_loss, batch_num = 0, 0
#     for batch in tqdm(eval_dataloader, total=len(eval_dataloader), desc="Eval ppl"):
#         batch = tuple(t.to(args.device) for t in batch)
#         source_ids, target_ids = batch
#         source_mask = source_ids.ne(tokenizer.pad_token_id)
#         target_mask = target_ids.ne(tokenizer.pad_token_id)

#         with torch.no_grad():
#             if args.model_type == 'roberta':
#                 loss, _, _ = model(
#                     source_ids=source_ids, source_mask=source_mask,
#                     target_ids=target_ids, target_mask=target_mask
#                 )
#             else:
#                 outputs = model(
#                     input_ids=source_ids, attention_mask=source_mask,
#                     labels=target_ids, decoder_attention_mask=target_mask
#                 )
#                 loss = outputs[0]

#         eval_loss += loss.item()
#         batch_num += 1
#     eval_loss = eval_loss / batch_num
#     eval_ppl = round(np.exp(eval_loss), 5)
#     return eval_ppl


def eval_bleu_epoch(args, eval_data, eval_examples, model, tokenizer, split_tag, criteria):
    logger.info("  ***** Running bleu evaluation on {} data*****".format(split_tag))
    logger.info("  Num examples = %d", len(eval_examples))
    logger.info("  Batch size = %d", args.eval_batch_size)
    eval_sampler = SequentialSampler(eval_data)
    if args.data_num == -1:
        eval_dataloader = DataLoader(
            eval_data, sampler=eval_sampler, batch_size=args.eval_batch_size, num_workers=4, pin_memory=True
        )
    else:
        eval_dataloader = DataLoader(eval_data, sampler=eval_sampler, batch_size=args.eval_batch_size)

    model.eval()
    pred_ids = []
    bleu, codebleu = 0.0, 0.0
    for batch in tqdm(eval_dataloader, total=len(eval_dataloader), desc="Eval bleu for {} set".format(split_tag)):
        source_ids = batch[0].to(args.device)
        source_mask = source_ids.ne(tokenizer.pad_token_id)
        with torch.no_grad():
            if args.model_type == 'roberta':
                preds = model(source_ids=source_ids, source_mask=source_mask)
                top_preds = [pred[0].cpu().numpy() for pred in preds]
            else:
                preds = model.generate(source_ids,
                                       attention_mask=source_mask,
                                       use_cache=True,
                                       num_beams=args.beam_size,
                                       early_stopping=args.task == 'summarize',
                                       max_length=args.max_target_length)
                top_preds = list(preds.cpu().numpy())
            pred_ids.extend(top_preds)
    # pdb.set_trace()
    pred_nls = [tokenizer.decode(id, skip_special_tokens=True, clean_up_tokenization_spaces=False) for id in pred_ids]

    output_fn = os.path.join(args.res_dir, "{}.output".format(split_tag))
    gold_fn = os.path.join(args.res_dir, "{}.gold".format(split_tag))
    src_fn = os.path.join(args.res_dir, "{}.src".format(split_tag))

    if args.task in ['defect']:
        target_dict = {0: 'false', 1: 'true'}
        golds = [target_dict[ex.target] for ex in eval_examples]
        eval_acc = np.mean([int(p == g) for p, g in zip(pred_nls, golds)])
        result = {'em': eval_acc, 'bleu': 0, 'codebleu': 0}

        with open(output_fn, 'w') as f, open(gold_fn, 'w') as f1, open(src_fn, 'w') as f2:
            for pred_nl, gold in zip(pred_nls, eval_examples):
                f.write(pred_nl.strip() + '\n')
                f1.write(target_dict[gold.target] + '\n')
                f2.write(gold.source.strip() + '\n')
            logger.info("Save the predictions into %s", output_fn)
    else:
        dev_accs, predictions = [], []
        with open(output_fn, 'w', encoding='utf8') as f, \
                open(gold_fn, 'w', encoding='utf8') as f1, \
                open(src_fn, 'w', encoding='utf8') as f2:
            for pred_nl, gold in zip(pred_nls, eval_examples):
                dev_accs.append(pred_nl.strip() == gold.target.strip())
                if args.task in ['summarize']:
                    predictions.append(str(gold.idx) + '\t' + pred_nl)
                    f.write(str(gold.idx) + '\t' + pred_nl.strip() + '\n')
                    f1.write(str(gold.idx) + '\t' + gold.target.strip() + '\n')
                    f2.write(str(gold.idx) + '\t' + gold.source.strip() + '\n')
                else:
                    f.write(pred_nl.strip() + '\n')
                    f1.write(gold.target.strip() + '\n')
                    f2.write(gold.source.strip() + '\n')

        if args.task in ['summarize']:
            (goldMap, predictionMap) = smooth_bleu.computeMaps(predictions, gold_fn)
            bleu = round(smooth_bleu.bleuFromMaps(goldMap, predictionMap)[0], 2)
        else:
            bleu = round(_bleu(gold_fn, output_fn), 2)
            # if split_tag == 'test' and args.task in ['refine', 'translate', 'concode']:
            #     codebleu = calc_code_bleu.get_codebleu(
            #         gold_fn, output_fn, args.lang,
            #         txt_ref=True,
            #         keyword_dir='../evaluation/CodeBLEU/keywords'
            #     )

        em = np.mean(dev_accs) * 100
        result = {'em': em, 'bleu': bleu}
        # if not args.task == 'summarize' and split_tag == 'test':
        #     result['codebleu'] = codebleu * 100

    logger.info("***** Eval results *****")
    for key in sorted(result.keys()):
        logger.info("  %s = %s", key, str(round(result[key], 4)))

    return result


def main():
    parser = argparse.ArgumentParser()
    args = add_args(parser)
    args.cpu_cont=1
    logger.info(args)
    t0 = time.time()

    set_dist(args)
    set_seed(args)
    config, model, tokenizer = build_or_load_gen_model(args)
    model.to(args.device)
    if args.n_gpu > 1:
        # for DataParallel
        model = torch.nn.DataParallel(model)
    pool = multiprocessing.Pool(args.cpu_cont)
    args.train_filename, args.dev_filename, args.test_filename = get_filenames(args.data_dir, args.task, args.sub_task)
    # fa = open(os.path.join(args.output_dir, 'summary.log'), 'a+')

    if args.do_train:
        if args.local_rank in [-1, 0] and args.data_num == -1:
            summary_fn = './tensorboard/{}'.format('/'.join(args.output_dir.split('/')[1:]))
            tb_writer = SummaryWriter(summary_fn)

        # Prepare training data loader
        train_examples, train_data = load_and_cache_gen_data(args, args.train_filename, pool, tokenizer, 'train')
        train_sampler = RandomSampler(train_data) if args.local_rank == -1 else DistributedSampler(train_data)
        train_dataloader = DataLoader(
            train_data,
            sampler=train_sampler,
            batch_size=args.train_batch_size,
            num_workers=0,
            pin_memory=False
        )

        # Prepare optimizer and schedule (linear warmup and decay)
        no_decay = ['bias', 'LayerNorm.weight']
        optimizer_grouped_parameters = [
            {
                'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
                'weight_decay': args.weight_decay
            },
            {
                'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)],
                'weight_decay': 0.0
            }
        ]
        optimizer = AdamW(optimizer_grouped_parameters, lr=args.learning_rate, eps=args.adam_epsilon)
        num_train_optimization_steps = len(train_dataloader) // args.gradient_accumulation_steps * args.num_train_epochs
        scheduler = get_linear_schedule_with_warmup(
            optimizer,
            num_warmup_steps=args.warmup_steps,
            num_training_steps=num_train_optimization_steps
        )

        # Start training
        logger.info("***** Running training *****")
        logger.info("  Num examples = %d", len(train_examples))
        logger.info("  Num Epochs = %d", args.num_train_epochs)
        logger.info("  Instantaneous batch size per GPU = %d", int(np.ceil(args.train_batch_size / args.n_gpu)))
        logger.info("  Total train batch size (w. parallel, distributed & accumulation) = %d",
                    args.train_batch_size * args.gradient_accumulation_steps * (
                        torch.distributed.get_world_size() if args.local_rank != -1 else 1))
        logger.info("  Gradient Accumulation steps = %d", args.gradient_accumulation_steps)
        logger.info("  Total optimization steps = %d", num_train_optimization_steps)

        dev_dataset = {}
        global_step, best_bleu_em, best_ppl = 0, -1, 1e6
        not_loss_dec_cnt, not_bleu_em_inc_cnt = 0, 0 if args.do_eval_bleu else 1e6

        for cur_epoch in range(args.start_epoch, int(args.num_train_epochs)):
            bar = tqdm(train_dataloader, total=len(train_dataloader), desc="Training")
            nb_tr_examples, nb_tr_steps, tr_loss = 0, 0, 0
            model.train()
            for step, batch in enumerate(bar):
                batch = tuple(t.to(args.device) for t in batch)
                source_ids, target_ids = batch
                source_mask = source_ids.ne(tokenizer.pad_token_id)
                target_mask = target_ids.ne(tokenizer.pad_token_id)

                if args.model_type == 'roberta':
                    loss, _, _ = model(source_ids=source_ids, source_mask=source_mask,
                                       target_ids=target_ids, target_mask=target_mask)
                else:
                    outputs = model(input_ids=source_ids, attention_mask=source_mask,
                                    labels=target_ids, decoder_attention_mask=target_mask)
                    loss = outputs[0]

                if args.n_gpu > 1:
                    loss = loss.mean()  # mean() to average on multi-gpu.
                if args.gradient_accumulation_steps > 1:
                    loss = loss / args.gradient_accumulation_steps
                tr_loss += loss.item()

                nb_tr_examples += source_ids.size(0)
                nb_tr_steps += 1
                loss.backward()

                if nb_tr_steps % args.gradient_accumulation_steps == 0:
                    # Update parameters
                    optimizer.step()
                    optimizer.zero_grad()
                    scheduler.step()
                    global_step += 1
                    train_loss = round(tr_loss * args.gradient_accumulation_steps / (nb_tr_steps + 1), 4)
                    bar.set_description("[{}] Train loss {}".format(cur_epoch, round(train_loss, 3)))

            # if args.do_eval:
            #     # Eval model with dev dataset
            #     if 'dev_loss' in dev_dataset:
            #         eval_examples, eval_data = dev_dataset['dev_loss']
            #     else:
            #         eval_examples, eval_data = load_and_cache_gen_data(args, args.dev_filename, pool, tokenizer, 'dev')
            #         dev_dataset['dev_loss'] = eval_examples, eval_data

            #     eval_ppl = eval_ppl_epoch(args, eval_data, eval_examples, model, tokenizer)
            #     result = {'epoch': cur_epoch, 'global_step': global_step, 'eval_ppl': eval_ppl}
            #     for key in sorted(result.keys()):
            #         logger.info("  %s = %s", key, str(result[key]))
            #     logger.info("  " + "*" * 20)
            #     if args.data_num == -1:
            #         tb_writer.add_scalar('dev_ppl', eval_ppl, cur_epoch)

            #     # save last checkpoint
            #     if args.save_last_checkpoints:
            #         last_output_dir = os.path.join(args.output_dir, 'checkpoint-last')
            #         if not os.path.exists(last_output_dir):
            #             os.makedirs(last_output_dir)
            #         model_to_save = model.module if hasattr(model, 'module') else model
            #         output_model_file = os.path.join(last_output_dir, "pytorch_model.bin")
            #         torch.save(model_to_save.state_dict(), output_model_file)
            #         logger.info("Save the last model into %s", output_model_file)

            #     if eval_ppl < best_ppl:
            #         not_loss_dec_cnt = 0
            #         logger.info("  Best ppl:%s", eval_ppl)
            #         logger.info("  " + "*" * 20)
            #         fa.write("[%d] Best ppl changed into %.4f\n" % (cur_epoch, eval_ppl))
            #         best_ppl = eval_ppl

            #         # Save best checkpoint for best ppl
            #         output_dir = os.path.join(args.output_dir, 'checkpoint-best-ppl')
            #         if not os.path.exists(output_dir):
            #             os.makedirs(output_dir)
            #         if args.always_save_model:
            #             model_to_save = model.module if hasattr(model, 'module') else model
            #             output_model_file = os.path.join(output_dir, "pytorch_model.bin")
            #             torch.save(model_to_save.state_dict(), output_model_file)
            #             logger.info("Save the best ppl model into %s", output_model_file)
            #     else:
            #         not_loss_dec_cnt += 1
            #         logger.info("Ppl does not decrease for %d epochs", not_loss_dec_cnt)
            #         if all([x > args.patience for x in [not_bleu_em_inc_cnt, not_loss_dec_cnt]]):
            #             early_stop_str = "[%d] Early stop as not_bleu_em_inc_cnt=%d, and not_loss_dec_cnt=%d\n" % (
            #                 cur_epoch, not_bleu_em_inc_cnt, not_loss_dec_cnt
            #             )
            #             logger.info(early_stop_str)
            #             fa.write(early_stop_str)
            #             break
            #     logger.info("***** CUDA.empty_cache() *****")
            #     torch.cuda.empty_cache()
            #     if args.do_eval_bleu:
            #         eval_examples, eval_data = load_and_cache_gen_data(
            #             args, args.dev_filename, pool, tokenizer, 'dev', only_src=True, is_sample=True
            #         )
            #         result = eval_bleu_epoch(args, eval_data, eval_examples, model, tokenizer, 'dev', 'e%d' % cur_epoch)
            #         dev_bleu, dev_em = result['bleu'], result['em']
            #         if args.task in ['summarize']:
            #             dev_bleu_em = dev_bleu
            #         elif args.task in ['defect']:
            #             dev_bleu_em = dev_em
            #         else:
            #             dev_bleu_em = dev_bleu + dev_em
            #         if args.data_num == -1:
            #             tb_writer.add_scalar('dev_bleu_em', dev_bleu_em, cur_epoch)
            #             # tb_writer.add_scalar('dev_em', dev_em, cur_epoch)
            #         if dev_bleu_em > best_bleu_em:
            #             not_bleu_em_inc_cnt = 0
            #             logger.info("  [%d] Best bleu+em: %.2f (bleu: %.2f, em: %.2f)",
            #                         cur_epoch, dev_bleu_em, dev_bleu, dev_em)
            #             logger.info("  " + "*" * 20)
            #             best_bleu_em = dev_bleu_em
            #             fa.write("[%d] Best bleu+em changed into %.2f (bleu: %.2f, em: %.2f)\n" % (
            #                 cur_epoch, best_bleu_em, dev_bleu, dev_em))
            #             # Save best checkpoint for best bleu
            #             output_dir = os.path.join(args.output_dir, 'checkpoint-best-bleu')
            #             if not os.path.exists(output_dir):
            #                 os.makedirs(output_dir)
            #             if args.data_num == -1 or args.always_save_model:
            #                 model_to_save = model.module if hasattr(model, 'module') else model
            #                 output_model_file = os.path.join(output_dir, "pytorch_model.bin")
            #                 torch.save(model_to_save.state_dict(), output_model_file)
            #                 logger.info("Save the best bleu model into %s", output_model_file)
            #         else:
            #             """
            #             --do_train  --do_eval  --save_last_checkpoints  --always_save_model  --task translate  --sub_task python-java --model_type codet5  --tokenizer_name roberta-base  --tokenizer_path .\bpe --output_dir .\g4g\python2java\paraphrase --num_train_epochs 100 --warmup_steps 100 --learning_rate 5e-5 --patience 5  --data_dir .\g4g\python2java\paraphrase --cache_path .\g4g\python2java\paraphrase\cached_data  --res_dir .\g4g\python2java\paraphrase --train_batch_size 1 --gradient_accumulation_steps 8 --eval_batch_size 2 --max_source_length 510 --max_target_length 510 --beam_size 1 --model_name_or_path .\codet5_base
            #             """

            #             not_bleu_em_inc_cnt += 1
            #             logger.info("Bleu does not increase for %d epochs", not_bleu_em_inc_cnt)
            #             if all([x > args.patience for x in [not_bleu_em_inc_cnt, not_loss_dec_cnt]]):
            #                 stop_early_str = "[%d] Early stop as not_bleu_em_inc_cnt=%d, and not_loss_dec_cnt=%d\n" % (
            #                     cur_epoch, not_bleu_em_inc_cnt, not_loss_dec_cnt)
            #                 logger.info(stop_early_str)
            #                 fa.write(stop_early_str)
            #                 break
            logger.info("***** CUDA.empty_cache() *****")
            torch.cuda.empty_cache()

        if args.local_rank in [-1, 0] and args.data_num == -1:
            tb_writer.close()
        logger.info("Finish training and take %s", get_elapse_time(t0))

    if args.do_test:
        logger.info("  " + "***** Testing *****")
        logger.info("  Batch size = %d", args.eval_batch_size)

        for criteria in ['best-bleu', 'best-ppl']:  # 'best-bleu', 'best-ppl', 'last'
            file = os.path.join(args.output_dir, 'checkpoint-{}/pytorch_model.bin'.format(criteria))
            if os.path.isfile(file):
                logger.info("Reload model from {}".format(file))
                model.load_state_dict(torch.load(file))
                eval_examples, eval_data = load_and_cache_gen_data(
                    args, args.test_filename, pool, tokenizer, 'test', only_src=True, is_sample=False
                )
                result = eval_bleu_epoch(args, eval_data, eval_examples, model, tokenizer, 'test', criteria)
                test_bleu, test_em = result['bleu'], result['em']
                test_codebleu = result['codebleu'] if 'codebleu' in result else 0
                result_str = "[%s] bleu-4: %.2f, em: %.4f, codebleu: %.4f\n" % (
                    criteria, test_bleu, test_em, test_codebleu
                )
                logger.info(result_str)
                # fa.write(result_str)
                if args.res_fn:
                    with open(args.res_fn, 'a+') as f:
                        f.write('[Time: {}] {}\n'.format(get_elapse_time(t0), file))
                        f.write(result_str)
    logger.info("Finish and take {}".format(get_elapse_time(t0)))
    # fa.write("Finish and take {}".format(get_elapse_time(t0)))
    # fa.close()


if __name__ == "__main__":
    main()
