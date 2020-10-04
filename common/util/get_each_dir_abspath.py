# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-29 15:39
@Author: guozg 
@File：get_each_dir_abspath.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import os
# import sys
# sys.path.append('../../common')
#
# from common.util.get_file_path import GetFilePath

class GetEachDirPath():
    '''获取每个目录的路径'''

    __case = 'case'
    __case_data = 'case/data'
    __common ='common'
    __common_config = 'common/config'
    __common_cookie = 'common/cookie'
    __common_excel = 'common/excel'
    __common_mail = 'common/mail'
    __common_method = 'common/method'
    __common_request = 'common/request'
    __common_util = 'common/util'
    __config = 'config'
    # __config_file_name='run_property.ini'
    __data = 'data'
    __data_cookie = 'data/cookie'
    __data_request = 'data/request'
    __driver = 'driver'
    __driver_log ='driver/log'
    __img = 'img'
    __po_base = 'po_base'
    __po_page = 'po_page'
    __report = 'report'
    __case_log = 'report/case_log'
    __testsuite = 'testsuite'
    __template = 'template'
    __upload_file = 'upload_file'
    __download_file = 'download_file'

    def __init__(self):
        # 项目所在的目录的根目录，项目名称所在的目录。如py3_ddt_po_autotest
        self.proj_dir = self.__get_proj_dir()

    def __cur_dir(self):
        ''''''
        cur_path = os.path.abspath(os.path.realpath(__file__))
        cur_dir = os.path.dirname(cur_path)
        return cur_dir

    def __get_proj_dir(self):
        ''''''
        dir = self.__cur_dir()
        root_dir = os.path.dirname(os.path.dirname(dir))
        return root_dir

    def get_case_dir(self):
        '''获取case的目录路径'''
        case_dir = os.path.abspath(os.path.join(self.proj_dir,self.__case))
        return case_dir

    def get_case_data_dir(self):
        '''
        获取case目录下的data的目录路径  \n
        该目录主要是用于存放用例case数据  \n
        :return: case目录下的data的目录路径
        '''
        case_data_dir = os.path.abspath(os.path.join(self.proj_dir,self.__case_data))
        return case_data_dir

    def get_common_dir(self):
        '''获取common目录的路径'''
        common_dir = os.path.abspath(os.path.join(self.proj_dir,self.__common))
        return common_dir

    def get_common_config_dir(self):
        '''
        获取 common目录下的 config 目录路径  \n
        config目录下的文件，主要是读取 配置ini文件的数据  \n
        :return: common目录下的 config 目录路径
        '''
        common_config_dir = os.path.abspath(os.path.join(self.proj_dir,self.__common_config))
        return common_config_dir

    def get_common_cookie_dir(self):
        '''
        获取common目录下的cookie的目录路径  \n
        cookie 目录下的文件主要是用于 操作cookie数据  \n
        return: common 目录下的cookie目录路径
        '''
        common_cookie_dir = os.path.abspath(os.path.join(self.proj_dir,self.__common_cookie))
        return common_cookie_dir

    def get_common_excel_dir(self):
        '''
        获取common 目录下的excel目录路径  \n
        excel目录下的文件主要是用于操作 excel数据  \n
        :return: common 目录下的excel目录路径
        '''
        common_excel_dir = os.path.abspath(os.path.join(self.proj_dir,self.__common_excel))
        return common_excel_dir

    def get_common_mail_dir(self):
        '''
        获取 common目录下的mail目录路径 \n
        mail目录下的文件 主要是进行 发送邮件 \n
        :return: common目录下的 mail目录路径
        '''
        common_mail_dir = os.path.abspath(os.path.join(self.proj_dir,self.__common_mail))
        return common_mail_dir

    def get_common_method_dir(self):
        '''
        获取 common目录下的 method目录路径  \n
        method目录下的文件 主要是执行 post or get请求  \n
        :return: common目录下的 method目录路径
        '''
        common_method_dir = os.path.abspath(os.path.join(self.proj_dir,self.__common_method))
        return common_method_dir

    def get_common_request_dir(self):
        '''
        获取 common目录下的 request 目录路径  \n
        request目录下的文件 主要是用于操作 request请求的json文件  \n
        :return: common目录下的 request目录路径
        '''
        common_request_dir = os.path.abspath(os.path.join(self.proj_dir,self.__common_request))
        return common_request_dir

    def get_common_util_dir(self):
        '''
        获取 common目录下的 util目录路径  \n
        util目录下的文件 主要是为各种操作提供服务  \n
        :return: common目录下的 util目录路径
        '''
        common_util_dir = os.path.abspath(os.path.join(self.proj_dir,self.__common_util))
        return common_util_dir

    def get_config_dir(self):
        '''
        获取 存放config ini文件 目录路径  \n
        config目录下的文件 主要是存放配置文件  \n
        :return: config目录路径
        '''
        config_dir = os.path.abspath(os.path.join(self.proj_dir,self.__config))
        return config_dir

    # def get_config_file_name(self):
    #     return self.__config_file_name
    #
    # def get_config_file_path(self):
    #     ''''''
    #     return GetFilePath().get_file_path_ini(self.get_config_dir(),self.get_config_file_name())

    def get_data_dir(self):
        '''
        data目录下还有cookie 和request两个目录  \n
        该目录主要用于操作用例运行时，数据的读取与存取  \n
        :return: data目录路径
        '''
        data_dir = os.path.abspath(os.path.join(self.proj_dir,self.__data))
        return data_dir

    def get_data_cookie_dir(self):
        '''
        获取 data目录下的cookie 目录路径  \n
        cookie目录下的文件 主要是存放cookie数据(响应结果的cookie数据)  \n
        :return: data目录下的cookie 目录路径
        '''
        data_cookie_dir =os.path.abspath(os.path.join(self.proj_dir,self.__data_cookie))
        return data_cookie_dir

    def get_data_request_dir(self):
        '''
        获取 data目录下的 request目录路径  \n
        request目录下的文件 主要是存放request请求的json数据  \n
        :return: data目录下的 request目录路径
        '''
        data_request_dir = os.path.abspath(os.path.join(self.proj_dir,self.__data_request))
        return data_request_dir

    def get_driver_dir(self):
        '''
        获取 driver 目录路径  \n
        driver目录下的文件 主要是存放各个浏览器的驱动  \n
        :return: driver 目录路径
        '''
        driver_dir = os.path.abspath(os.path.join(self.proj_dir,self.__driver))
        return driver_dir

    def get_driver_log_dir(self):
        '''
        获取driver目录下 log日志输出目录  \n
        log目录下的文件主要为：各个浏览器的驱动输出日志。 \n
        :return: driver目录下的log日志输出目录
        '''
        driver_log_dir = os.path.abspath((os.path.join(self.proj_dir,self.__driver_log)))
        return driver_log_dir


    def get_img_dir(self):
        '''
        获取 img 目录路径  \n
        img目录下的文件 主要是存放手工截图  \n
        :return: img 目录路径
        '''
        img_dir = os.path.abspath(os.path.join(self.proj_dir,self.__img))
        return img_dir

    def get_report_dir(self):
        '''
        获取 report 目录路径  \n
        report目录下的文件 主要是存放 运行结果html文件  \n
        :return: report 目录路径
        '''
        report_dir = os.path.abspath(os.path.join(self.proj_dir,self.__report))
        return report_dir

    def get_case_log_dir(self):
        '''
        获取case log 目录路径  \n
        :return: case log目录路径
        '''
        case_log = os.path.abspath(os.path.join(self.proj_dir,self.__case_log))
        return case_log

    def get_po_base_dir(self):
        '''
        获取 po模式下的 base 目录路径  \n
        po_base目录下的文件 主要是对selenium一些常见的页面元素的操作，进行二次封装  \n
        :return: po_base 目录路径
        '''
        po_base_dir=os.path.abspath(os.path.join(self.proj_dir,self.__po_base))
        return po_base_dir

    def get_po_page_dir(self):
        '''
        获取 po模式下的 page 目录路径  \n
        po_page目录下的文件 主要是存放要操作的页面的页面元素属性  \n
        :return: po_page 目录路径
        '''
        po_page_dir=os.path.abspath(os.path.join(self.proj_dir,self.__po_page))
        return po_page_dir

    def get_template_dir(self):
        '''
        获取 template 目录路径  \n
        template目录下的文件 主要是为一些模板，如case 的excel模板  \n
        :return: template 目录路径
        '''
        template_dir = os.path.abspath(os.path.join(self.proj_dir,self.__template))
        return template_dir

    def get_testsuite_dir(self):
        '''
        执行所有用例的目录  \n
        :return: testsuite 的目录路径
        '''
        testsuite_dir = os.path.abspath(os.path.join(self.proj_dir,self.__testsuite))
        return testsuite_dir

    def get_upload_file_dir(self):
        '''
        获取上传文件的目录  \n
        :return: upload_file 的目录路径
        '''
        upload_file_dir = os.path.abspath(os.path.join(self.proj_dir,self.__upload_file))
        return upload_file_dir

    def get_download_file_dir(self):
        '''
        获取下载文件的目录  \n
        :return: download_file 的目录路径
        '''
        download_file_dir = os.path.abspath(os.path.join(self.proj_dir,self.__download_file))
        return download_file_dir


# a = GetEachDirPath()
# println(a.get_case_data_dir())
# println(a.get_report_dir())
# println(a.get_case_data_dir())
# println(a.get_common_cookie_dir())
# println(a.get_common_dir())
# println(a.get_upload_file_dir())
# println(a.get_download_file_dir())
# help(GetEachDirPath)
