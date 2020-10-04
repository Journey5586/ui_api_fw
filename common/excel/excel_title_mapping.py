# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-28 11:01
@Author: guozg 
@File：excel_title_mapping.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""


class ExcelTitleMapping():
    '''
    用例数据的表头映射值
    '''
    __case_id = 'case_id'
    __case_name = 'case_name'
    __case_desc = 'case_desc'
    __case_type = 'case_type'
    __url = 'url'
    __run_whether = 'run_whether'
    __method = 'method'
    __header = 'header'
    __save_cookie = 'save_cookie'
    __read_cookie_case_id = 'read_cookie_case_id'
    __rely_case_id = 'rely_case_id'
    __rely_data = 'rely_data'
    __request_rely_file = 'request_rely_file'
    __request_data = 'request_data'
    __expect_result = 'expect_result'
    __actual_result = 'actual_result'
    __pass_whether = 'pass_whether'
    __err_msg = 'err_msg'

    def get_case_id(self):
        '''用例id 表头'''
        return self.__case_id

    def get_case_name(self):
        '''用例名称 表头'''
        return self.__case_name

    def get_case_desc(self):
        '''用例描述 表头'''
        return self.__case_desc

    def get_case_type(self):
        '''用例类型(UI or App) 表头'''
        return self.__case_type

    def get_url(self):
        '''url 表头'''
        return self.__url

    def get_run_whether(self):
        '''用例是否运行 表头'''
        return self.__run_whether

    def get_method(self):
        '''请求方式 post or get  表头'''
        return self.__method

    def get_header(self):
        '''是否有hear请求 表头'''
        return self.__header

    def get_save_cookie(self):
        '''是否保存cookie 表头'''
        return self.__save_cookie

    def get_read_cookie_case_id(self):
        '''依赖的cookie 表头'''
        return self.__read_cookie_case_id

    def get_rely_case_id(self):
        '''依赖的case id 表头'''
        return self.__rely_case_id

    def get_rely_data(self):
        '''依赖的数据 表头'''
        return self.__rely_data

    def get_request_rely_file(self):
        '''请求要替换的数据对应的字段 表头'''
        return self.__request_rely_file

    def get_requst_data(self):
        '''请求数据 表头'''
        return self.__request_data

    def get_expect_result(self):
        '''预期结果 表头'''
        return self.__expect_result

    def get_actual_result(self):
        '''实际结果 表头'''
        return self.__actual_result

    def get_pass_whether(self):
        '''用例是否通过 表头'''
        return self.__pass_whether

    def get_err_msg(self):
        '''err msg  表头'''
        return self.__err_msg

# help(ExcelTitleMapping)