# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-29 15:11
@Author: guozg 
@File：opera_json_file.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import json
from common.util.get_each_dir_abspath import GetEachDirPath
from common.util.get_file_path import GetFilePath


class OperaJsonFile():
    '''操作json文件。'''

    def write_json_data(self, filepath, dict):
        '''
        将dict转化为string后，写入到json文件中，易传输  \n
        :param filepath: 文件路径，包括文件名
        :param dict: 要写入的字典值
        :return: None
        '''
        filepath = filepath
        # 判断是否以.json结束
        if filepath != None and filepath != '':
            filepath = filepath if filepath.endswith('.json') else filepath + '.json'

        with open(filepath, 'w', encoding='utf-8') as fp:
            # dict转化为string并存入到json文件中
            fp.write(json.dumps(dict))

    def write_dict_to_json_file(self, filepath, dict):
        '''
        直接将dict写入到json文件中(将dict转化为json字符串格式，写入文件)，易存储  \n
        :param filepath: 文件路径
        :param dict: 要写入的字典
        :return: None
        '''
        filepath = filepath
        # 判断是否是以.json结束
        if filepath != None and filepath != '':
            filepath = filepath if filepath.endswith('.json') else filepath + '.json'
        # println(filepath,dict)
        with open(filepath, 'w', encoding='utf-8') as fp:
            # 直接将字典写入到json文件中
            json.dump(dict, fp)

    def read_json_data(self, filepath) -> dict:
        '''
        读取json文件中的值，将转化为dict，针对内存中的对象，将string转化为dict对象  \n
        :param filepath: 文件路径,包含文件名
        :return: 转化的dict
        '''
        filepath = filepath

        if filepath != None and filepath != '':
            filepath = filepath if filepath.endswith('.json') else filepath + '.json'

        with open(filepath, 'r', encoding='utf-8') as fp:
            # 将string转化为dict
            return json.loads(fp.read())

    def read_json_file_to_dict(self, filepath) -> dict:
        '''
        读取json文件，并将数据转化为dict,针对文件句柄，是直接从文件中读取  \n
        :param filepath: 文件路径,包含文件名
        :return: 转化后的dict
        '''
        filepath = filepath
        if filepath != None and filepath != '':
            filepath = filepath if filepath.endswith('.json') else filepath + '.json'
        with open(filepath, 'r', encoding='utf-8') as fp:
            return json.load(fp)

    def read_json_file(self, filename):
        '''
        读取json文件，并将数据转化为dict,针对文件句柄，是直接从文件中读取  \n
        :param filename: 文件名
        :return: 转化后的dict
        '''
        dir_path = GetEachDirPath()
        file_path = GetFilePath()
        # 获取依赖的数据所在的目录
        data_dir = dir_path.get_data_request_dir()
        # 拼接数据目标文件路径(启文件名称)
        json_file = file_path.get_file_path_json(data_dir, filename)
        # 获取json文件数据
        with open(json_file, 'r', encoding='utf-8') as fp:
            return json.load(fp)


# help(OperaJsonFile)