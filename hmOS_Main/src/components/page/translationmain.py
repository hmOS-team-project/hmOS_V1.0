


import TranslateFunction as translation

from flask import Flask,request

from flask_cors import CORS,cross_origin
import json
 
app=Flask(__name__)
 

@app.route("/test1",methods=["GET"])
@cross_origin()
def check():

    # 默认返回内容
    return_dict= {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data=request.args.to_dict()
    source_code=get_data.get('source_code')
    prefix=get_data.get('prefix')
    id = get_data.get('id')
    print(source_code)
    print(prefix)
    print(id)
    # 对参数进行操作
    return_dict['result']=get_result(source_code, prefix, id)
    print(return_dict)
    return json.dumps(return_dict, ensure_ascii=False)
 


def get_result(source_code, prefix, id):
    result, FINAL_length = hm.get_res_by_pc_based_hmCodeTrans(source_code, prefix, id, 'p2j')
    return result



    
if __name__ == "__main__":
    hm = translation.hmCodeTrans()
    
    app.run(debug=True, use_reloader=False)