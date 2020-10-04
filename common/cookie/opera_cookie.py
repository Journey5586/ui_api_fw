# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-29 16:30
@Author: guozg 
@File：opera_cookie.py
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

sys.path.append('../../')
from common.util.get_each_dir_abspath import GetEachDirPath
from common.util.opera_json_file import OperaJsonFile
from common.util.get_file_path import GetFilePath

class OperaCookie():
    '''
    操作cookie，主要为以下三方面的内容：  \n
    1：将cookie值保存到json文件中  \n
    2：从保存的cookie 的json文件中读取cookie数据  \n
    3：将cookie值转化为dict 字典  \n
    '''


    def __init__(self):
        '''
        进行实例化时，会进行如下操作：  \n
        1：获取保存cookie数据的目录  \n
        2：实例化获取文件path对象  \n
        3：实例化操作json文件对象  \n
        '''
        self.cookie_dir = GetEachDirPath().get_data_cookie_dir()
        self.file_path = GetFilePath()
        self.opera_file = OperaJsonFile()

    def save_cookie_to_file(self, case_id, response):
        '''
        获取请求的响应结果中的cookie，并将值保存到json文件中，以便其他用例需要   \n
        :param case_id: 保存cookie的json文件名称，与case id同名
        :param response: 请求的响应结果，该结果中有存放了cookie，使用response.cookies 获取
        :return: None
        '''
        cookie_name = case_id
        # 拼接cookie的路径(含文件名称)
        cookie_path = self.file_path.get_file_path_json(self.cookie_dir, cookie_name)
        # 将cookie转化为dict
        cookie_dict = self.cookie_to_dict(response.cookies)
        # println(case_id,cookie_dict,cookie_path)
        # 将cookie写入到json文件中
        self.opera_file.write_dict_to_json_file(cookie_path,cookie_dict)

    def get_cookie_from_json_file(self,case_id):
        '''
        从json文件中读取保存过的所依赖的cookie  \n
        :param case_id: 原则上cookie 的json文件的名称与case id保持一致
        :return: 获取到的cookie值，类型为dict
        '''
        cookie_name = case_id
        # 拼接文件路径
        cookie_path = self.file_path.get_file_path_json(self.cookie_dir,cookie_name)
        # 获取数据
        cookie_dict = self.opera_file.read_json_file_to_dict(cookie_path)
        return cookie_dict

    def cookie_to_dict(self,cookie):
        '''
        将获取到的cookie值转化为dict  \n
        :param cookie: cookie值
        :return: 转化为dict后的cookie值
        '''
        return requests.utils.dict_from_cookiejar(cookie)

