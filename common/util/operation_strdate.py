# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-11-07 20:33
@Author: guozg 
@File：operation_strdate.py
@Description: 
1.操作日期字符串
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import sys

sys.path.append('../../')

from common.util.character_replace import CharacterReplace as cp


class OperaStrDate():
    '''
    操作日期字符串，如"2019-10-10,2019-10-12",将日期字符串切割为数组  \n
    可以将切割后的数组再进行排序  \n
    '''

    def __init__(self, strdate_value):
        '''
        实例化时，必须传入日期字符串，日期之间使用英文的逗号进行分隔 \n
        :param strdate_value: 日期字符串，如"2019-10-10,2019-10-12"
        '''
        self.strdate = strdate_value
        # 格式化日期字符串
        self.strdate = self.format_date()

    def format_date(self):
        '''
        格式化日期字符串，将日期之间的分隔符统一为英语逗号  \n
        :return: 格式化后的日期字符串
        '''
        datevalue = self.strdate
        # 将所有的中英文分号、中文逗号、中文顿号全部替换为英文 逗号
        datevalue = cp().all_to_English_comma(datevalue)

        return datevalue

    def strdate_to_list(self) -> list:
        '''
        将日期字符串切割为list  \n
        :return: list
        '''
        date_list = self.strdate.split(',')
        return date_list

    def date_sort(self, asc=True) -> list:
        '''
        日期数组排序，默认为升序  \n
        :param asc: bool，True表示升序，False为降序
        :return: 排序后的list
        '''
        date_list = self.strdate_to_list()
        if asc == True:
            date_sort = sorted(date_list, reverse=False)
        else:
            date_sort = sorted(date_list, reverse=True)

        return date_sort

    def strdate_sort(self, asc=True) -> str:
        '''
        对日期字符进行排序处理，默认为升序   \n
        处理思路如下：  \n
        1：先进行格式化，调用fromat_date()方法  \n
        2：将str转化为list 调用strdate_to_list()方法  \n
        3：对list进行排序，调用date_sort()方法  \n
        4：对回返的list进行拼接为str，并返回   \n
        :param asc: 默认为升级，当为False时，为降序
        :return: str
        '''
        date_sort = self.date_sort(asc)
        count = len(date_sort)
        comma = ','
        tmp = ''
        strdate = ''
        for i in range(count):
            tmp = date_sort[i]
            if i < count - 1:
                strdate = strdate + tmp + comma
            else:
                strdate = strdate + tmp

        return strdate

# if __name__ == '__main__' :
#     strdate = '2019-11-10,2019-11-12,2019-11-01,2019-11-02,2019-11-21'
#     osd = OperaStrDate(strdate)
#     println(osd.strdate_sort())

# help(OperaStrDate)