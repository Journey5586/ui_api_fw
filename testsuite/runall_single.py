# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-30 10:07
@Author: guozg 
@File：runall_single.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""

# from BeautifulReport import BeautifulReport
import unittest
import sys
import os

sys.path.append('../')
from common.util.get_each_dir_abspath import GetEachDirPath
from common.mail.send_mail import SendMail
from common.util.get_file_path import GetFilePath
from common.util.get_time import GetTime
from common.report.BeautifulReport_Single import BeautifulReport
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

# 从配置文件里获取相关的配置信息
case_name_rule = config.get_case_name_rule()
report_name = config.get_report_html_name()
report_title = config.get_report_title()

# ****************拼接报告名称(含路径)*************************
cur_time = GetTime().get_cur_time()
report_name = report_name + cur_time
report_path = file_path.get_file_path_html(report_dir, report_name)

# 收集所要执行的case
discover = unittest.TestLoader().discover(case_dir, case_name_rule)
# println(discover)
# 执行目标所有的用例，并获取相应的结果
res = BeautifulReport(discover)
# 设置相应的报告标题，报告名称，报告目录，图片目录。
res.report(report_title, report_name, report_dir, img_dir)

# 统计数据
pass_count = res.success_count
fail_count = res.failure_count
err_count = res.error_count
skip_count = res.skipped
# 这是只添加了一个html报告附件
# att_file = report_path


excel_name = config.get_excel_name()
sheet_name = config.get_excel_sheet_name()

ini_name = 'run_property.ini'

excel_path = file_path.get_file_path_xlsx(excel_dir, excel_name)
req_json_file_path = file_path.get_file_path_json(req_json_dir, sheet_name)

config_file_path = file_path.get_file_path_ini(config_dir, ini_name)

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


SendMail().send_main_rpt(pass_count, fail_count, err_count, skip_count, att_file)
