# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-9-2 23:02
@Author: guozg 
@File：get_match_data.py
@Description: 
1. 该类下的所有功能 均是为opera_rely_data.py服务的
2. 主要用于从response data里 获取想要的依赖数据。
@Modify Time:  
@Modify Description: 
1.
2.
"""
# 要安装的包为 jsonpath-rw
from jsonpath_rw import parse
import json


class GetMatchData():
    '''
    获取匹配到的数据，主要是为opera_rely_data.py服务的。
    '''


    def __init__(self,resp_json_dumps_str,rely_data_key):
        '''
        要传入response.json的 dumps 为str的值，以及 excel表中的rely data  \n
        :param resp_json_dumps_str: json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2)
        :param rely_data_key:
        '''
        self.resp = resp_json_dumps_str
        self.rely_data = rely_data_key

    def get_match_data(self):
        '''
        从请求的响应的结果中，获取相应的依赖数据
        :return: 从响应结果中获取到的依赖数据。
        '''
        rely_data_value = None

        if self.resp !=None:
            # 将临时的str响应结果转化为字典，方便查找
            res_dict = json.loads(self.resp)

            jsonpath_expr = parse(self.rely_data)
            find_data = jsonpath_expr.find(res_dict)
            # 获取所依赖的响应结果数据
            rely_data_value = [match.value for match in find_data][0]
            # 在print()语句里加<p>是为了在BreatifulReport html报告里，能正常的显示为一行数据，否则就会连接在一块，很难查看有用数据
            print('<p>--- 所依赖的数据对应的key为【 %s 】 对应的响应结果的值为：【 %s 】' % (self.rely_data, rely_data_value))

        return rely_data_value

    def get_replace_req_data(self, req_data_dict, rely_req_file):
        '''
        替换请求数据 ，需要传入 request json请求 dict数据，以及要替换的数据的key  \n
        即：将请求数据中的某值替换为所依赖的数据。  \n
        :param req_data_dict: 读取的request json请求数据 为dict
        :param rely_req_file: 想要替换的请求数据所对应的字段
        :return: 替换后的结果 dict
        '''
        rely_data_value = self.get_match_data()

        req_data_dict[rely_req_file] = rely_data_value
        print('<p>--- 要替换的key为：', rely_req_file)
        print('<p>--- 更新后的请求数据：', req_data_dict)

        return  req_data_dict


# help(GetMatchData)