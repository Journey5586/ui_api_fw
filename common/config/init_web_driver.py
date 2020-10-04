# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-11-05 16:58
@Author: guozg 
@File：init_web_driver.py
@Description: 
1. 初始化 web driver
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
from selenium import webdriver
import sys
sys.path.append('../')
import os
from common.config.read_config_data import GetConfigFileData
from common.util.get_file_path import GetFilePath
from common.util.get_each_dir_abspath import GetEachDirPath
from common.util.get_time import GetTime

# 获取当前时间
cur_time = GetTime().get_cur_time()

config = GetConfigFileData()
# 获取要运行的浏览器
browser = config.get_driver_browser()
# 获取驱动 exe
chrome_driver_exe = config.get_driver_chrome_exe_name()
firefox_driver_exe = config.get_driver_firefox_exe_name()
ie_driver_exe = config.get_driver_ie_exe_name()

# 获取driver相关的目录，及日志输出目录
driver_log_dir = GetEachDirPath().get_driver_log_dir()
driver_dir = GetEachDirPath().get_driver_dir()

# 设置浏览器驱动exe的路径
chrome_exe_path = GetFilePath().get_file_path_exe(driver_dir, chrome_driver_exe)
firefox_exe_path = GetFilePath().get_file_path_exe(driver_dir, firefox_driver_exe)
ie_exe_path = GetFilePath().get_file_path_exe(driver_dir, ie_driver_exe)

# 设置各浏览器驱动输出的log名称
chrome_log_name = 'chrome_log' + cur_time
firefox_log_name = 'firefox_log' + cur_time
ie_log_name = 'ie_log' + cur_time


# 设置各浏览器的log路径
chrome_log_path = GetFilePath().get_file_path_log(driver_log_dir, chrome_log_name)
firefox_log_path = GetFilePath().get_file_path_log(driver_log_dir, firefox_log_name)
ie_log_path = GetFilePath().get_file_path_log(driver_log_dir, ie_log_name)



class InitWebDriver():
    '''
    初始化Web端Driver
    '''
    def init_driver(self)->webdriver:
        '''
        初始化 driver，并返回 driver  \n
        :return: driver
        '''
        if browser == 'ie':
            driver = webdriver.Ie(executable_path=ie_exe_path, log_level='WARNING', log_file=ie_log_path)
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=firefox_exe_path, service_log_path=firefox_log_path)
        else:
            # opinion = webdriver.ChromeOptions()
            # opinion.binary_location = chrome_exe_path
            # print(chrome_exe_path)
            # print(opinion)
            # driver = webdriver.Chrome(service_log_path=chrome_log_path,chrome_options=opinion)
            driver = webdriver.Chrome(executable_path=chrome_exe_path,service_log_path=chrome_log_path)
        return driver

# aa = InitWebDriver()
# # print('---------',aa.init_driver().name,'-------------')
# driver = aa.init_driver().name
# print(driver,len(driver),driver == 'chrome')
