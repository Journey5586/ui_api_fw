# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-09-03 10:46
@Author: guozg 
@File：response_json_to_str.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import json


class ResJsonToStr():
    '''
    将请求的响应结果的json串转化为str
    '''

    def get_res_json_to_str(self, response):
        '''传入接口的响应结果'''
        res_json_str = json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2)
        return res_json_str


# help(ResJsonToStr)