# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-11-07 10:45
@Author: guozg 
@File：character_replace.py
@Description: 
1.对一些特定的字符时行替换
2.根据需要将中文标点符号替换为英文，或将英文的标点符号替换为中文
@Modify Time:  
@Modify Description: 
1.
2.
"""


class CharacterReplace():
    '''
    对一些标点字符进行替换，中文字符替换为英文的字符，或将英文字符替换为中文字符等。 \n
    逗号","：comma  \n
    分号";"：semicolon  \n
    冒号":": colon  \n
    '''

    def semicolon_Chinese_to_English(self, values):
        '''
        将中文状态下的分号转化为英文状态的分号  \n
        :param values: 要替换字符所在的文本值
        :return: 替换后的结果
        '''
        value = values
        if '；' in values:
            value = values.replace('；', ';')
        return value

    def comma_Chinese_to_English(self, values):
        '''
        将中文状态下的逗号转化为英文状态的分号  \n
        :param values: 要替换字符所在的文本值
        :return: 替换后的结果
        '''
        value = values
        if '，' in values:
            value = values.replace('，', ',')
        return value

    def semicolon_English_to_Chinese(self, values):
        '''
        将英文状态下的分号转化为中文状态下的分号  \n
        :param values: 要替换字符所在的文本值
        :return: 替换后的结果
        '''
        value = values
        if ';' in values:
            value = values.replace(';', '；')
        return value

    def comma_English_to_Chinese(self, values):
        '''
        将英文状态下的逗号转化为中文状态下的逗号  \n
        :param values: 要替换字符所在的文本值
        :return: 替换后的结果
        '''
        value = values
        if '，' in values:
            value = values.replace('，', ',')
        return value

    def colon_Chinese_to_English(self, values):
        '''
        将中文状态下的冒号转化为英文下的冒号  \n
        :param values: 要替换字符所在的文本值
        :return: 替换后的结果
        '''
        value = values
        if '：' in values:
            value = values.replace('：', ':')
        return value

    def colon_English_to_Chinese(self, values):
        '''
        将英文状态下的冒号转化为中文下的冒号  \n
        :param values: 要替换字符所在的文本值
        :return: 替换后的结果
        '''
        value = values
        if ':' in values:
            value = values.replace(':', '：')
        return value

    def character_Chinese_to_English(self, values, character_old, character_new):
        '''
        自定义将中文状态下的字符替换为英文状态下的字符  \n
        :param values: 要替换字符所在的文本值
        :param character_old: 要替换的字符(中文状态下的标点符号)
        :param character_new: 替换后的字符(英文状态下的标点符号)
        :return: 替换后的结果
        '''
        value = values
        old = character_old
        new = character_new
        if old in values:
            value = values.replace(old, new)
        return value

    def character_English_to_Chinese(self, values, character_old, character_new):
        '''
        自定义将英文的字符替换为中文状态下的字符  \n
        :param values: 要替换字符所在的文本值
        :param character_old: 要替换的字符(英文状态下的标点符号)
        :param character_new: 替换后的字符(中文状态下的标点符号)
        :return: 替换后的结果
        '''
        value = values
        old = character_old
        new = character_new
        if old in values:
            value = values.replace(old, new)
        return value

    def character_customize_to_English(self, values, character_old, character_new):
        '''
        自定义将任意状态下的字符替换为英文状态下的字符  \n
        :param values: 要替换字符所在的文本值
        :param character_old: 要替换的字符(中文状态下的标点符号)
        :param character_new: 替换后的字符(英文状态下的标点符号)
        :return: 替换后的结果
        '''
        value = values
        old = character_old
        new = character_new
        if old in values:
            value = values.replace(old, new)
        return value

    def character_customize_to_Chinese(self, values, character_old, character_new):
        '''
        自定义将任意状态下字符替换为中文状态下的字符  \n
        :param values: 要替换字符所在的文本值
        :param character_old: 要替换的字符(英文状态下的标点符号)
        :param character_new: 替换后的字符(中文状态下的标点符号)
        :return: 替换后的结果
        '''
        value = values
        old = character_old
        new = character_new
        if old in values:
            value = values.replace(old, new)
        return value

    def all_to_English_comma(self,values):
        '''
        将所有的中英文的分号，中文的逗号，中文的顿号"，；;、"全部替换为英文的逗号  \n
        :param values: 要替换字符所在的文本值
        :return: 替换后的结果
        '''
        value = values
        # 逗号
        comma = ','
        value =value.replace(';',comma).replace('；',comma).replace('，',comma).replace('、',comma)
        return value

    def all_to_English_semicolon(self,values):
        '''
        将所有的中英文的逗号、中文的分号、中文的顿号", ； ，、"全部替换为英文的分号  \n
        :param values: 要替换字符所在的文本值
        :return: 替换后的结果
        '''
        value = values
        # 分号
        semicolon = ';'
        value = value.replace(',',semicolon).replace('，',semicolon).replace('、',semicolon).replace('；',semicolon)
        return value

# help(CharacterReplace)