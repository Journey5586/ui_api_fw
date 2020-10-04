# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-09-03 16:06
@Author: guozg 
@File：run_case.py
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
from common.excel.get_excel_cell_value import GetCellValue
from common.request.get_request_data import GetReqData
from common.cookie.opera_cookie import OperaCookie
from common.excel.opera_rely_data import OperaRelyData
from common.method.run_method import RunMethod


class RunCase():
    '''
    运行用例，该类主要用到case中。 \n
    该类中获取相关的请求数据，并进行执行  \n
    '''

    # def __init__(self, sheetname, json_file_path, excel_data, excel_dict):
    #     '''
    #     实例化时，要传入sheet表的名称，请求的json文件路径，获取的sheet表的数据(list类型,值为dict)，sheet表数据(双层dict)  \n
    #     excel data 为 [{一行数据(含表头)},{一行数据(含表头)},{一行数据(含表头)}]  \n
    #     excel_dict 为 双层dict，{'case id value':{一行数据(含表头)},'case id value':{一行数据(含表头)}}  \n
    #     :param sheetname: sheet表的名称
    #     :param json_file_path: json文件的路径(含名称)
    #     :param excel_data: dict类型，值为@data(*excel_list)的每一行的结果(也为dict)
    #     :param excel_dict: 双层dict，sheet表的所有数据，外层的key为 case id 的值，key对应的值为 dict(一行数据)
    #     '''
    #
    #     self.sheet_name = sheetname
    #     self.json_file_path = json_file_path
    #     # self.json_data = GetReqData(self.json_file_path)
    #     self.json_data = GetReqData()
    #     self.excel_data = excel_data
    #     self.excel_dict = excel_dict

    def __init__(self, excel_data, excel_dict):
        '''
        实例化时，要传入获取的sheet表的数据(list类型,值为dict)，sheet表数据(双层dict)  \n
        excel data 为 [{一行数据(含表头)},{一行数据(含表头)},{一行数据(含表头)}]  \n
        excel_dict 为 双层dict，{'case id value':{一行数据(含表头)},'case id value':{一行数据(含表头)}}  \n

        :param excel_data: dict类型，值为@data(*excel_list)的每一行的结果(也为dict)
        :param excel_dict: 双层dict，sheet表的所有数据，外层的key为 case id 的值，key对应的值为 dict(一行数据)
        '''

        self.json_data = GetReqData()
        self.excel_data = excel_data
        self.excel_dict = excel_dict


    def run_case(self):
        '''
        运行用例，该用例会将用例执行时，所需要的数据全部获取到，然后去执行  \n
        :return: 用例的执行结果，即response的结果。
        '''

        cell_value = GetCellValue(**self.excel_data)
        # 开始获取各个单元格的数据
        case_id = cell_value.get_case_id()
        case_type = cell_value.get_case_type()
        url = cell_value.get_url()
        '''
        在这里不需要获取 ：
        1：用例是否运行，在外层已经判断了，即：调用该方法的，表示该条用例都是需要运行的
        2：不需要获取依赖的数据，即 excel表中的 rely_data的值，在获取所有依赖数据的时候已经获取了。
        3：不需要获取预期结果，预期结果是调整的函数或用例 去获取，是要进行结果判断的。
        '''
        method = cell_value.get_method()
        header = cell_value.get_header()
        save_cookie = cell_value.get_save_cookie()
        rely_cookie_case_id = cell_value.get_rely_cookie_case_id()
        rely_case_id = cell_value.get_rely_case_id()
        # rely_data = cell_value.get_rely_data()
        request_rely_file = cell_value.get_request_rely_file()
        request_data = self.json_data.get_data(cell_value.get_requst_data())
        # expect_result = cell_value.get_expect_result()

        # header后续内容再补充
        if header == 'yes':
            header = None
        else:
            header = None
        cookie = None
        # 判断是否为空
        if rely_cookie_case_id !=None and rely_cookie_case_id != '':
            cookie = OperaCookie().get_cookie_from_json_file(rely_cookie_case_id)
        # 判断是否为空
        if rely_case_id !=None and rely_case_id !='':
            rep_data = OperaRelyData(case_id, rely_case_id, **self.excel_dict).get_all_rely_data()
            # 替换请求中的数据
            request_data[request_rely_file] = rep_data

        print('<p>--- case id  is :', case_id, '--method--', method, '--url--', url, '--request_data--', request_data)
        res = RunMethod().run_main(method, url, request_data, header, cookie)
        print('case id is :',case_id,'===========','save cookie is :',save_cookie)
        if save_cookie == 'yes':
            print('<p>------此时的 savecookie为：',save_cookie)
            OperaCookie().save_cookie_to_file(case_id, res)

        return res


# help(RunCase)