# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-01-08 10:07
@Author: 郭志国 
@File：runall_multithreading.py
@Description: 
1.该文件是针对多线程执行case所编写的，不适合单线程执行
2.若是单线程执行，请使用runall_single.py
3.
@Modify Time:  
@Modify Description: 
1.
2.
"""

import time
import unittest
import sys
import os
import threading
from threading import Thread, local

sys.path.append('../')
from common.util.get_each_dir_abspath import GetEachDirPath
from common.mail.send_mail import SendMail
from common.util.get_file_path import GetFilePath
from common.util.get_time import GetTime
from common.report.BeautifulReport_MultiThreading import BeautifulReport
from common.config.read_config_data import GetConfigFileData

# 获取相应的路径，文件名称规则。
dir = GetEachDirPath()
file_path = GetFilePath()
config = GetConfigFileData()

case_dir = dir.get_case_dir()
excel_dir = dir.get_case_data_dir()
report_dir = dir.get_report_dir()
img_dir = dir.get_img_dir()
req_json_dir = dir.get_data_request_dir()
config_dir = dir.get_config_dir()

# ****************获取case名称规则、html报告相关的配置************
# 从配置文件里获取相关的配置信息
case_name_rule = config.get_case_name_rule()
report_name = config.get_report_html_name()
report_title = config.get_report_title()

# *********** 要上传的部分附件***********************
excel_name = config.get_excel_name()
sheet_name = config.get_excel_sheet_name()
# 获取excel的路径(含名称)
excel_path = file_path.get_file_path_xlsx(excel_dir, excel_name)
# 获取excel对应的json文件的路径(含名称)
req_json_file_path = file_path.get_file_path_json(req_json_dir, sheet_name)

# 配置文件的名称
ini_name = 'run_property.ini'
# 获取配置文件ini的路径(含名称)
config_file_path = file_path.get_file_path_ini(config_dir, ini_name)

# ****************拼接报告名称(含路径)*************************
cur_time = GetTime().get_cur_time()
report_name = report_name + cur_time
report_path = file_path.get_file_path_html(report_dir, report_name)

# *********************邮件中的统计数据***********************
# 用户统计数据
pass_count = 0
fail_count = 0
err_count = 0
skip_count = 0

# *********************多线程的线程变量***********************
# threading中的local用于取代全局变量
# 主要用于线程只能读写自己的数据，不会相互干扰。
tlocal = local()
# 用于存放运行结果，如{线程名称:运行结果}
dict_res = {}

# ******************beautifulreport中的 FIELDS[]统计相关的key************
# beautifulreport 中的FIELDS[]中的统计数据对应的key
test_all_key = 'testAll'
test_pass_key = 'testPass'
test_fail_key = 'testFail'
test_error_key = 'testError'
test_skip_key = 'testSkip'


def collect_testsuite():
    '''
    收集所要执行的testsuite  \n
    :return: 返回相应的收集结果
    '''
    # 收集所要执行的case
    discover = unittest.TestLoader().discover(case_dir, case_name_rule)
    # println(discover)
    return discover


def run_testsuite(testsuite,lock):
    '''
    运行相应的testsuite  \n
    注：支持多线程
    :param testsuite: 测试套件
    :return: None
    '''
    global dict_res
    # 执行目标所有的用例，并获取相应的结果
    time.sleep(1)

    # 每个线程存储各自的实例化 beautifulreport
    tlocal.res = BeautifulReport(testsuite)
    # 获取当前线程的名称
    thread_name = threading.current_thread().getName()
    # 将当前的线程名称及实例化存储到字典中
    dict_res[thread_name] = tlocal.res
    # 运行当前的testsuite
    tlocal.res.report(report_title, report_name, report_dir, img_dir)



def runres_to_report():
    '''
    将运行的结果输出到html报告中 \n
    :return: None
    '''
    global pass_count, fail_count, err_count, skip_count, dict_res

    # 先计算出成功、失败、报错、跳过的用例的个数
    for key in dict_res:
        res = dict_res[key]
        pass_count += res.success_count
        fail_count += res.failure_count
        err_count += res.error_count
        skip_count += res.skipped

    testAll = pass_count + fail_count + err_count + skip_count
    # 第二次循环，将结果写入到报告中，并更改 html报告中的统计数据

    for key in dict_res:
        res = dict_res[key]
        # 更改结果中的统计数据
        res.FIELDS[test_pass_key] = pass_count
        res.FIELDS[test_fail_key] = fail_count
        res.FIELDS[test_error_key] = err_count
        res.FIELDS[test_skip_key] = skip_count
        res.FIELDS[test_all_key] = testAll

        # 写入报告
        res.output_report()
        print(res.result_list)


def get_att_file():
    '''
    获取要上传的附件 \n
    :return: 返回相关的附件
    '''

    # 这是添加html报告、case excel表、request请求 json文件、config配置文件
    att_file = [report_path, excel_path, req_json_file_path, config_file_path]

    # ************** 获取request目录下的所有json文件**********************
    # 获取case目录下的所有的py文件,返回数据为list
    py_files = os.listdir(case_dir)

    # ******************* 第一步：先获取case目录下的 所有py文件，同时去掉__init__.py文件 ************************
    # 去掉 case 目录下的 __init__py文件
    py_init = '__init__.py'
    if py_init in py_files:
        py_files.remove(py_init)
    # 先对list进行过滤，保留所有的文件，去掉所有的目录
    py_file_list = []

    for py_file in py_files:

        py_path = os.path.join(case_dir, py_file)

        if os.path.isdir(py_path):
            print('当前为目录：', py_path)
        # 当不是目录时，就肯定是文件
        # 进行切割返回为路径名和文件扩展名的数组
        elif os.path.splitext(py_path)[-1] == '.py':
            py_file_list.append(py_file)

    # ************** 第二步： 根据 run_property.ini里的 要运行的case规则，来定位要执行的py文件 ***************************
    '''
    要执行的case规则，格式主要有以下几种：
    1:  XXX*XXXX.py  (表示以XXX开头的，以XXXX结尾的，中间是任意字符的py文件)
    2:  XXXX*   (表示以XXXX开头的，任意文件)
    3:  *XXXX.py    (表示以XXXX结尾的，任意py文件)
    4:  XXXX    (表示执行XXXX文件)
    所以从上可以看出，要么使用*号 来执行匹配的文件，要么不使用*号，直接指定文件
    '''
    # 必须将 list的值拷贝给变量，否则在修改变量中的值时，会修改list中的值。
    py_file_list_tmp = py_file_list.copy()
    character = '*'
    if character in case_name_rule:
        case_name_rule_list = case_name_rule.split(character)
        # 将所有的字母全部转化为小写
        start_rule = case_name_rule_list[0].lower()
        end_rule = case_name_rule_list[-1].lower()
        # 循环过滤掉非目标py文件
        for file in py_file_list_tmp:
            # 对py的文件名进行一次字母转化为小写
            file_tmp = file.lower()
            if file_tmp.startswith(start_rule) and file_tmp.endswith(end_rule):
                pass
            # 表示为非要执行的py文件，需要移除
            else:
                py_file_list.remove(file)
    # 表示要执行特定的py文件
    else:
        # 先转化为小写
        file_name = case_name_rule.lower()

        for file in py_file_list:

            # 将字母转化为小写
            file_tmp = file.lower()
            if file_name == file_tmp:

                pass
            else:
                py_file_list.remove(file)

    # ****************** 第三步：将目标py文件对应的json文件找到，并返回 **********************
    # 检测json文件是否存在
    for item in py_file_list:
        item = item.replace('.py', '.json')
        json_file = os.path.abspath(os.path.join(req_json_dir, item))

        if os.path.exists(json_file):
            # 当检测到json文件存在时，直接保存(在最后发送邮件地，要上传该附件)
            att_file.append(json_file)
            print('该文件将会被上传：', json_file)
        else:
            print('该json文件不存在：', json_file)
    # 返回要上传的附件列表
    return att_file


def send_mail():
    '''
    将最终的运行结果发送邮件给相关的人员  \n
    :return: None
    '''
    global pass_count, fail_count, err_count, skip_count
    # 获取要上传的附件列表
    att_file = get_att_file()
    # 发送相关的邮件
    SendMail().send_main_rpt(pass_count, fail_count, err_count, skip_count, att_file)


if __name__ == '__main__':
    # 获取要执行的测试套件集
    suites = collect_testsuite()
    # 线程列表
    threads = []
    # 空的testsuite对应的字符串的值
    suite_value_none = '<unittest.suite.TestSuite tests=[]>'
    lock = threading.Lock()
    # 要剔除掉空的testsuite
    for suite in suites:
        # 获取testsuite对应的str值
        suite_str_value = suite.__str__()
        # 当testsuite不为空时，才会去执行
        if suite_value_none != suite_str_value:
            # 创建线程,并执行要执行的哪个方法，并传入该方法相应的参数
            # target:要运行的方法的名称，args:该方法要传入的参数，注必须为tuple
            t = Thread(target=run_testsuite, args=(suite,lock,))
            # 将线程添加到线程list中
            threads.append(t)

    # print(threads)

    # 依次启动每个线程。
    for thread in threads:
        thread.start()
        print('start----------', thread.getName())

    # 让主线程等待所有的子线程执行结束
    for thread in threads:
        # 在等待之前，先判断子线程是否是活动状态。
        if thread.is_alive():
            thread.join()

    time.sleep(1)

    # 获取当前的所有线程
    threadlist = threading.enumerate()
    print('当前的线程列表为：', threadlist)
    for item in threadlist:
        print('线程为：%s --线程的名称为：%s --线程是否为活动状态：%s' % (item, item.getName(), item.is_alive()))

    # 将运行结果输出到html报告中
    runres_to_report()
    print(sys.stdout)
    # 发送邮件
    send_mail()
