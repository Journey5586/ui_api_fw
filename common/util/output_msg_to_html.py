# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-12-18 10:24
@Author: guozg 
@File：output_msg_to_html.py
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


class Output():
    '''
    将日志输出到html报告中,支持多线程。 \n
    即在业务case脚本中，可以将平时使用print打印的语句，换成str_msg，输出到当前线程id为名称的txt中.  \n
    需要注意的是：txt的创建、txt中的内容读取、txt内容的清空、txt文件的删除 均在BeautifulReport_MultiThreading.py文件中  \n
    而本脚本是将我们在脚本中的写好的之前由print输出的消息，写入到txt文件中。当脚本在执行过程中发生错误或失败时，此时  \n
    是由BeautifulReport_MultiThreading.py 向xt文件中写入这些错误或失败信息。
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
        实际上是将这些日志写入到以当前线程id为名称的txt文件中  \n
        而将txt文件中的内容读取并输入到html中，是在BeautifulReport_MutilThreading.py脚本中控制完成的  \n
        :param strmsg: 字符串类型
        :return: None
        '''

        # print('-----【',strmsg,'】-----',end="")
        # print('--【{},{}】--'.format(strmsg, threading.current_thread().getName()))
        # print('--【{}】--'.format(strmsg))

        # thread_name = threading.current_thread().getName()
        # txt_name = thread_name + '.txt'
        # 由于thread的name会出现重名的情况，尤其是多进程下又有多线程的情况，百分百会出现重名。

        thread_name = threading.current_thread().getName()
        main_thread = 'MainThread'

        # 先判断是单线程，还是多线程，若是单线程，则直接print
        if thread_name == main_thread:
            print('-----【',str(strmsg),'】-----')


        else:

            thread_id = str(threading.current_thread().ident)
            txt_name = thread_id + '.txt'
            log_path = epath().get_case_log_dir()
            txt_path = os.path.join(log_path, txt_name)
            with open(txt_path, 'a', encoding='utf8') as fp:
                fp.write(str(strmsg))
                fp.write('\n')

    # def tuple_msg(self, *tuple_msg):
    #     '''
    #     将tuple类型的信息输出到html报告中  \n
    #     :param tuple_msg: tuple类型的信息
    #     :return: None
    #     '''
    #     print('-----【', *tuple_msg, '】-----')
    #
    # def dict_msg(self, dict_msg: dict):
    #     '''
    #     将dict类型的信息输出到html报告中  \n
    #     dict类型的信息可以直接使用str类型的信息进行输出  \n
    #     :param dict_msg: dict类型的信息
    #     :return: None
    #     '''
    #     print('-----【', dict_msg, '】-----')

# help(Output)