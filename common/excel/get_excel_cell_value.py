# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-28 11:35
@Author: guozg 
@File：get_excel_cell_value.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import sys

sys.path.append('../../')
from common.excel.excel_title_mapping import ExcelTitleMapping


class GetCellValue():
    '''获取sheet表中的 各个单元格的数据'''

    def __init__(self, **kwargs):
        '''
        传入sheet表中的第一行数据(含表头)  类型为dict  \n
        :param kwargs: dict
        '''
        self.dict = kwargs
        self.etm = ExcelTitleMapping()

    def get_case_id(self):
        '''获取 用例 id'''
        return self.dict[self.etm.get_case_id()]

    def get_case_name(self):
        '''获取 用例名称'''
        return self.dict[self.etm.get_case_name()]

    def get_case_desc(self):
        '''获取 用例描述'''
        return self.dict[self.etm.get_case_desc()]

    def get_case_type(self):
        '''
        用例类型(UI or App)，该列是否需要，有待验证，同时也方便后续扩展  \n
        建议不增加该列，该列最后极有可能是无用的  \n
        默认值及为空时，均为api  \n
        :return: api 或 ui
        '''
        case_type = 'api'
        value = self.dict[self.etm.get_case_type()]
        if value == None:
            case_type = 'api'
        elif ('u' in value) or ('U' in value):
            case_type = 'ui'
        else:
            case_type = 'api'

        return case_type

    def get_url(self):
        '''获取 url'''
        return self.dict[self.etm.get_url()]

    def get_run_whether(self):
        '''
        用例是否执行，默认值及为空时，均为 yes  \n
        :return: yes 或 no
        '''
        run_whether = 'yes'
        value = self.dict[self.etm.get_run_whether()]
        if value == None:
            run_whether = 'yes'
        elif ('n' in value) or ('N' in value):
            run_whether = 'no'

        return run_whether

    def get_method(self):
        '''
        获取接口请求类型，这里是否需要进行默认赋值为post，有待验证  \n
        建议：还是默认为post请求。  \n
        因为UI的数据依赖，仍然是接口的数据依赖和cookie依赖，ui有数据依赖时，被依赖的  \n
        用例的执行方式和接口的方式一样。  \n
        即：case_type 也不需要有，没有必要  \n
        :return: get 或 post 或 None
        '''
        method = None
        value = self.dict[self.etm.get_method()]
        if value == None:
            method = None
        elif ('g' in value) or ('G' in value):
            method = 'get'
        elif ('p' in value) or ('P' in value):
            method = 'post'

        return method

    def get_header(self):
        '''
        是否有header  \n
        目前由于接口中没有header相关的验证，所以没有写该方法，后续补充  \n
        在后续补充时，需要再写一个header相关的配置，当为yes时，进行调用  \n
        默认值或为空时，均为 no  \n
        :return: yes  或 no
        '''
        header = 'no'
        value = self.dict[self.etm.get_header()]
        if value == None:
            header = 'no'
        elif ('y' in value) or ('Y' in value):
            header = 'yes'

        return header

    def __header_data(self):
        ''''''
        pass

    def get_save_cookie(self):
        '''
        是否保存cookie  \n
        默认是不需要保存cookie的  \n
        即：默认值及为空时，均为 no  \n
        :return: yes 或 no
        '''
        save_cookie = 'no'
        value = self.dict[self.etm.get_save_cookie()]
        if value == None:
            save_cookie = 'no'
        elif ('y' in value) or ('Y' in value):
            save_cookie = 'yes'

        return save_cookie

    def get_rely_cookie_case_id(self):
        '''获取依赖的cookie所对应的case id '''
        return self.dict[self.etm.get_read_cookie_case_id()]

    def get_rely_case_id(self):
        '''获取所依赖的数据 所对应的case id'''
        return self.dict[self.etm.get_rely_case_id()]

    def get_rely_data(self):
        '''获取所依赖的数据(请求响应结果中的数据)所对应的key'''
        return self.dict[self.etm.get_rely_data()]

    def get_request_rely_file(self):
        '''获取所要替换的请求数据所对应的key'''
        return self.dict[self.etm.get_request_rely_file()]

    def get_requst_data(self):
        '''获取请求数据'''
        return self.dict[self.etm.get_requst_data()]

    def get_expect_result(self):
        '''获取预期结果'''
        return self.dict[self.etm.get_expect_result()]

    def get_actual_result(self):
        '''获取实际结果'''
        return self.dict[self.etm.get_actual_result()]

    def get_pass_whether(self):
        '''获取用例是否通过'''
        return self.dict[self.etm.get_pass_whether()]

    def get_err_msg(self):
        '''获取err msg'''
        return self.dict[self.etm.get_err_msg()]

# help(GetCellValue)