# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-09-03 10:45
@Author: guozg 
@File：compare_data.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""

class CompData():

    def is_contain(self,search,pattern):
        """
        判断一个字符串是否在另外一个字符串中

        :param search: 查找的字符串
        :param pattern: 被查找的字符串
        :return: True 或False
        """
        flag = None
        # 判断预期结果与实际结果是否相等
        if search in pattern:
            flag = True
        else :
            flag = False
        return flag

# help(CompData)