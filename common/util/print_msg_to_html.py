# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-12-18 10:24
@Author: guozg 
@File：print_msg_to_html.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import threading
import os, sys

sys.path.append('../../')
from common.util.get_each_dir_abspath import GetEachDirPath as epath


class PrintMsgToHtml():
    '''
    将日志输出到html报告中,暂时未使用
    '''

    # def print_str_msg(self,strmsg):
    #     '''
    #     将字符串类型的日志输出到html报告中  \n
    #     :param strmsg: 字符串类型
    #     :return: None
    #     '''
    #     println('-----【',strmsg,'】-----')
    #
    # def print_tuple_msg(self,*tuple_msg):
    #     '''
    #     将tuple类型的信息输出到html报告中  \n
    #     :param tuple_msg: tuple类型的信息
    #     :return: None
    #     '''
    #     println('-----【',*tuple_msg,'】-----')
    #
    # def print_dict_msg(self,dict_msg:dict):
    #     '''
    #     将dict类型的信息输出到html报告中  \n
    #     :param dict_msg: dict类型的信息
    #     :return: None
    #     '''
    #     println('-----【',dict_msg,'】-----')
    #
    def str_msg(self, strmsg):
        '''
        将字符串类型的日志输出到html报告中  \n
        :param strmsg: 字符串类型
        :return: None
        '''

        # print('-----【',strmsg,'】-----',end="")
        # print('--【{},{}】--'.format(strmsg, threading.current_thread().getName()))
        # print('--【{}】--'.format(strmsg))

        # thread_name = threading.current_thread().getName()
        # txt_name = thread_name + '.txt'
        # 由于thread的name会出现重名的情况，尤其是多进程下又有多线程的情况，百分百会出现重名。
        thread_id = str(threading.current_thread().ident)
        txt_name = thread_id + '.txt'
        log_path = epath().get_case_log_dir()
        txt_path = os.path.join(log_path, txt_name)
        with open(txt_path, 'a', encoding='utf8') as fp:
            fp.write(str(strmsg))
            fp.write('\n')

    def tuple_msg(self, *tuple_msg):
        '''
        将tuple类型的信息输出到html报告中  \n
        :param tuple_msg: tuple类型的信息
        :return: None
        '''
        print('-----【', *tuple_msg, '】-----')

    def dict_msg(self, dict_msg: dict):
        '''
        将dict类型的信息输出到html报告中  \n
        dict类型的信息可以直接使用str类型的信息进行输出  \n
        :param dict_msg: dict类型的信息
        :return: None
        '''
        print('-----【', dict_msg, '】-----')

# help(PrintMsgToHtml)
