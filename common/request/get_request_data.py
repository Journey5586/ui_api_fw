# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-29 15:09
@Author: guozg 
@File：get_request_data.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import sys,os
sys.path.append('../../')

from common.util.opera_json_file import OperaJsonFile
from common.config.read_config_data import GetConfigFileData
from common.util.get_each_dir_abspath import GetEachDirPath
from common.util.get_file_path import GetFilePath

class GetReqData():
    '''获取request的请求数据。'''

    # def __init__(self,json_file_path):
    #     '''要传入request 请求对应的json路径(含文件名)'''
    #     self.json_path = json_file_path
    #     self.opera_json_file = OperaJsonFile()
    #     self.data = self.__read_data()

    def __init__(self):
        '''
        通过读取ini配置文件，来获取对应的json文件名称  \n
        再通过获取json文件的dir 进行拼接相关的路径  \n
        即：不需要再通过参数传递json path
        '''
        self.json_path = self.get_json_file_path()
        self.opera_json_file = OperaJsonFile()
        self.data = self.__read_data()


    def __read_data(self):
        '''
        直接从josn文件读取数据，并转化为dict  \n
        :return: 转化后的dict
        '''
        data = self.opera_json_file.read_json_file_to_dict(self.json_path)
        return data

    def get_data(self,key):
        '''
        从json文件中获取相应的数据后，再获取指定key的值  \n
        :param key: 要获取值的字典key
        :return: 字典中key 对应的value
        '''
        return self.data[key]

    def get_json_file_path(self):
        '''
        获取request 请求对应的json文件路径(启文件名称)  \n
        :return: 获取request 请求对应的json文件路径(启文件名称)
        '''
        sheetname = GetConfigFileData().get_excel_sheet_name()
        json_dir = GetEachDirPath().get_data_request_dir()
        json_path = GetFilePath().get_file_path_json(json_dir, sheetname)
        return json_path

# help(GetReqData)