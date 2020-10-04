# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-09-02 16:29
@Author: guozg 
@File：get_time.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
from datetime import date,datetime

class GetTime():
    '''获取当前日期 及当前时间，输出为指定格式'''

    def get_cur_date(self):
        """
        获取当前客户端的日期，格式为 2017-01-01

        :return: 当前日期
        """
        # curdate = time.strftime("%Y-%m-%d")
        # return curdate
        curdate = date.strftime(datetime.now(), "%Y-%m-%d")
        return curdate


    def get_cur_time(self):
        '''
        获取当前客户端的时间，格式为 20190809 233320

        :return: 当前时间,时间格式为'%Y%m%d %H%M%S' 如20190909 233020
        '''
        curtime = datetime.strftime(datetime.now(), '%Y%m%d %H%M%S')
        return curtime

# help(GetTime)