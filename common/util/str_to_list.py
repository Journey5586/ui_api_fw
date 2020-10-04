# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-11-06 17:30
@Author: guozg 
@File：str_to_list.py
@Description: 
1. 将字符串切割为list
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import sys
sys.path.append('../../')

from common.util.character_replace import CharacterReplace as cp

class StrToList():
    '''
    将字符串的值切割为list，传入的字符串之间必须使用英文分号;进行切割
    '''

    def __init__(self,values):
        '''
        将传入的字符串切割为 list，并返回  \n
        :param values: 字符串，值与值之间必须使用英文的分号进行分隔 如 王妙海;许章洪;李大
        '''
        self.str_values = values

    def get_list_by_semicolon(self):
        '''
        将传入的字符串按 英文分号 ; 切割为list  \n
        先将里面的中英文逗号、中文分号、中文顿号 全部替换为 英文分号  \n
        然后再进行按分号进行切割  \n
        :return: list or str
        '''
        semicolon = ';'
        value = cp().all_to_English_semicolon(self.str_values)
        str_list = value.split(semicolon)

        return str_list

    def get_list_by_comma(self):
        '''
        将传入的字符串按英文 逗号 , 切割为list  \n
        先将里面的中英文分号、中文逗号、中文顿号 全部替换为 英文逗号号  \n
        然后再进行按分号进行切割  \n
        :return: list or str
        '''
        comma = ','
        value = cp().all_to_English_comma(self.str_values)
        str_list = value.split(comma)

        return str_list

# help(StrToList)