# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-09-16 11:09
@Author: guozg 
@File：app_config.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import configparser
import os,sys
sys.path.append('../')
from common.util.get_file_path import GetFilePath as filepath
from common.util.get_each_dir_abspath import GetEachDirPath as dirpath

class GetAppConfig():

    ''''''
    __file_name = 'app_config.ini'
    __node_caps = 'Caps'
    __platformName = 'platformName'
    # __udid = 'udid'
    __deviceName = 'deviceName'
    __automationName = 'automationName'
    __appPackage = 'appPackage'
    __appActivity = 'appActivity'
    __noReset = 'noReset'
    __url = 'url'
    __node_run = 'Run'
    __timeout = 'timeout'
    __environment = 'environment'

    def __init__(self):

        # dir = os.path.dirname(os.path.realpath(__file__))
        # file_dir = os.path.join(os.path.dirname(os.path.dirname(dir)),'config')
        file_dir = dirpath().get_config_dir()
        file_path = filepath().get_file_path_ini(file_dir,self.__file_name)

        self.__config = configparser.ConfigParser()
        self.__config.read(file_path, 'utf-8')

    def get_caps_platformName(self):
        ''''''
        return self.__config.get(self.__node_caps, self.__platformName)

    # def get_caps_udid(self):
    #     ''''''
    #     return self.__config.get(self.__node_caps, self.__udid)

    def get_caps_deviceName(self):
        ''''''
        return self.__config.get(self.__node_caps, self.__deviceName)

    def get_caps_automationName(self):
        ''''''
        return self.__config.get(self.__node_caps,self.__automationName)

    def get_caps_appPackage(self):
        ''''''
        return self.__config.get(self.__node_caps, self.__appPackage)

    def get_caps_appActivity(self):
        ''''''
        return self.__config.get(self.__node_caps, self.__appActivity)

    def get_caps_noReset(self):
        ''''''
        return self.__config.get(self.__node_caps, self.__noReset)

    def get_url(self):
        ''''''
        return self.__config.get(self.__node_caps, self.__url)

    def get_run_timeout(self):
        ''''''
        timeout = self.__config.get(self.__node_run, self.__timeout)
        if timeout == None :
            timeout = 2
        else :
            timeout = int(timeout)
            if timeout <=2:
                timeout = 2
            elif timeout >= 60:
                timeout = 60
            return timeout

    def get_run_environment(self):
        ''''''
        return self.__config.get(self.__node_run, self.__environment)



