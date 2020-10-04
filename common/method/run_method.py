# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-29 10:44
@Author: guozg 
@File：run_method.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import requests
import sys
sys.path.append('../')
from common.config.read_config_data import GetConfigFileData

timeout = GetConfigFileData().get_req_timeout()

class RunMethod():
    '''
    执行接口请求。
    '''

    def post(self, url, param, header=None, cookie=None,timeout=timeout):
        '''post请求'''
        res = None

        if header != None and cookie != None:
            res = requests.post(url=url, data=param, headers=header, cookies=cookie,timeout=timeout)
        elif header != None and cookie == None:
            res = requests.post(url=url, data=param, headers=header,timeout=timeout)
        elif header == None and cookie != None:
            res = requests.post(url=url, data=param, cookies=cookie,timeout=timeout)
        else:
            res = requests.post(url=url, data=param,timeout=timeout)

        return res

    def get(self, url, param, header=None, cookie=None,timeout=timeout):
        '''get请求'''
        res = None

        if header != None and cookie != None:
            res = requests.get(url=url, data=param, headers=header, cookies=cookie,timeout=timeout)
        elif header != None and cookie == None:
            res = requests.get(url=url, data=param,timeout=timeout)
        elif header == None and cookie != None:
            res = requests.get(url=url, data=param, cookies=cookie,timeout=timeout)
        else:
            res = requests.get(url=url, data=param,timeout=timeout)
        return res

    def run_main(self, method, url, param, header=None, cookie=None):
        '''执行接口请求的主方法'''
        res = None
        if method == "post":
            res = self.post(url, param, header, cookie,timeout=timeout)
        elif method =='get':
            res = self.get(url, param, header, cookie,timeout=timeout)
        # 没有必要增加此条判断
        # 当执行此方法时，表示是进行接口请求，post 或 get请求(最常见的两种)
        # UI自动化不走 该方法。
        else:
            print('你的用例为UI自动化用例，非接口用例！！！')
            res = None
        # 返回结果
        return res

# help(RunMethod)
