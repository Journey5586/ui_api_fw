# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-8-25 22:28
@Author: 郭志国 
@File：test_login.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
from ddt import ddt, data, file_data
import unittest
import os
import sys

sys.path.append('../')
from common.excel.read_excel_data import ReadExcelData
from common.config.read_config_data import GetConfigFileData
from common.util.get_each_dir_abspath import GetEachDirPath
from common.util.get_file_path import GetFilePath
from common.excel.get_excel_cell_value import GetCellValue
from common.request.get_request_data import GetReqData
from common.method.run_method import RunMethod
from common.excel.opera_rely_data import OperaRelyData
from common.cookie.opera_cookie import OperaCookie
# from common.excel.get_match_data import GetMatchData
from common.util.response_json_to_str import ResJsonToStr
from common.util.run_case import RunCase

'''
需要注意的是：
1：这里在获取excel的数据时，是需要传入excel的路径的。
2：该路径可以是绝对路径，也可以相对路径。
3：如果是相对路径，必须是调用/执行 该case(test_login.py)文件(runall.py)的相对路径，而不是相对于 test_login.py文件的相对路径
4：建议传入绝对路径，即获取当前 test_login.py的路径，然后再进行拼接。
'''

config_data = GetConfigFileData()
dir_path = GetEachDirPath()
file_path = GetFilePath()
# 想要读取的excel表的名称
excel_name = config_data.get_excel_name()
# sheet表的名称
sheet_name = config_data.get_excel_sheet_name()
# 获取excel所在的目录
excel_dir = dir_path.get_case_data_dir()
# 获取excel的路径(含名称)
excel_path = file_path.get_file_path_xlsx(excel_dir, excel_name)

excel_data = ReadExcelData(excel_path, sheet_name)
excel_list = excel_data.get_sheet_data_list()
excel_dict = excel_data.get_sheet_data_dict()

json_file_dir = dir_path.get_data_request_dir()
json_file_name = sheet_name
json_file_path = file_path.get_file_path_json(json_file_dir, json_file_name)

# json_data = GetReqData(json_file_path)
json_data = GetReqData()


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print()
        print('---用例开始！！！！---')
        print('该部分为接口测试用例，请耐心等待')

    @classmethod
    def tearDownClass(cls):
        print()
        print('---用例执行结束!!!!---')

    '''
    需要注意的地方：
    1：这个路径是相对于当前文件(test_login.py)的路径,不是相对于调用test_login.py的路径
    2：这里的参数名称，可以是具体的参数名，如username、password 等。
    3：当为具体的参数名时，需要注意的是 json文件里的每一行的参数的名称及个数必须保持一致。
    4：并且在这里要将所有的参数全部罗列出来。
    5：当json文件里的参数名称不一致时，建议使用不定长的参数，如字典类型，**kwargs
    6：当参数的不定长的字典参数时，在获取实际的值时，使用dict[参数名] 来获取
    7：由于file_data 会自动将 josn文件中的key(指下一行的login02) 去掉，拼接到了 case的名称里
    8："login02":{"username":"12345678002","password":"test1234","code":"123"}
    9：file_data 此时传过来的数据，是进行for循环，依次取一行的数据。这一行的数据(如上行所示)是一个字典
    10：json文件中的key 如login02 会保存到 self.__dict__['_testMethodName'] 中,如 test_login_json_2_login02
    11：使用self.__dict__['_testMethodName']或self.__dict__.get('_testMethodName') 可以获取实际的每个case的名称。
    '''

    @file_data(json_file_path)
    def test_login_json(self, **kwargs):
        dict = kwargs
        print(dict)
        username = dict['username']
        print('username is :', username)
        test_name = self.__dict__['_testMethodName']
        print(self.__dict__.get('_testMethodName'))
        print('test name is:', test_name)
        if username == 'login05':
            self.skipTest('测试跳过')
        elif username in ('18342100004', '18342100005'):
            self.assertEqual(username, '18342100004', '用户名不匹配')
            self.assertEqual(username, '18342100005', '用户名不匹配')
            # self.assertIn(username,'18342100004，18342100005','用户名不匹配')

    '''
    需要注意的地方：
    1：data里的excel_list 的值为list，而*excel_list是将list中的值取出来，一个解压的过程，在进行参数传递时可以这样写
    2：*excel_list 取出来的每个值均为dict
    3：进行for循环，每次取出的值是excel中一行的数据，其中key为 表头，value对应的具体的数据
    4：使用self.__dict__['_testMethodName']或self.__dict__.get('_testMethodName') 可以获取实际的每个case的名称。
    '''

    @data(*excel_list)
    def test_login_excel(self, excel_data):
        '''
        数据来源 为excel  \n
        :param excel_data: 传入的为一个字典,传入参数时 要将list进行解压，如 *list
        :return: None
        '''
        dict = excel_data
        case_id = dict['case_id']
        test_name = self.__dict__.get('_testMethodName')
        print(dict)
        print('case_id is :', case_id)
        print('test name is :', test_name)
        self.assertIn('0', case_id, '检测case id是否包括数字0')

    @data(*excel_list)
    def test_login_excel_api(self, excel_data):
        '''

        :param excel_data:
        :return:
        '''
        dict = excel_data
        print('<p>--- 该用例所在行的数据如下：---')
        print('<p>', dict)
        cell_value = GetCellValue(**dict)
        # 开始获取各个单元格的数据
        case_id = cell_value.get_case_id()
        case_type = cell_value.get_case_type()
        url = cell_value.get_url()
        run_whether = cell_value.get_run_whether()
        if run_whether == 'no':
            self.skipTest('该用例不执行')
        method = cell_value.get_method()
        header = cell_value.get_header()
        save_cookie = cell_value.get_save_cookie()
        rely_cookie_case_id = cell_value.get_rely_cookie_case_id()
        rely_case_id = cell_value.get_rely_case_id()
        rely_data = cell_value.get_rely_data()
        request_rely_file = cell_value.get_request_rely_file()
        request_data = json_data.get_data(cell_value.get_requst_data())
        expect_result = cell_value.get_expect_result()

        # header后续内容再补充
        if header == 'yes':
            header = None
        else:
            header = None
        cookie = None

        if rely_cookie_case_id != None and rely_cookie_case_id != '':
            cookie = OperaCookie().get_cookie_from_json_file(rely_cookie_case_id)

        if rely_case_id != None and rely_case_id != '':
            rep_data = OperaRelyData(case_id, rely_case_id, **excel_dict).get_all_rely_data()
            # 替换请求中的数据
            request_data[request_rely_file] = rep_data

        print('<p>--- case id  is :', case_id, '--method--', method, '--url--', url, '--request_data--', request_data)
        res = RunMethod().run_main(method, url, request_data, header, cookie)
        if save_cookie == 'yes':
            OperaCookie().save_cookie_to_file(case_id, res)

        actual_result = ResJsonToStr().get_res_json_to_str(res)
        self.assertIn(expect_result, actual_result, '预期结果不存在于实际结果中')

    @data(*excel_list)
    def test_login_excel_api_00(self, excel_data):
        '''
        将执行方法给独立出来，写成公共类。
        :param excel_data:
        :return:
        '''
        dict = excel_data
        print('<p>--- 该用例所在行的数据如下：---')
        print('<p>', dict)
        cell_value = GetCellValue(**dict)

        run_whether = cell_value.get_run_whether()
        if run_whether == 'no':
            self.skipTest('该用例不执行')

        expect_result = cell_value.get_expect_result()
        # 下面一行代码为执行方法，形成公共方法。
        # res = RunCase(sheet_name, json_file_path, dict, excel_dict).run_case()
        res = RunCase(dict, excel_dict).run_case()

        actual_result = ResJsonToStr().get_res_json_to_str(res)
        self.assertIn(expect_result, actual_result, '预期结果不存在于实际结果中')

if __name__ == '__main__':
    unittest.main()
