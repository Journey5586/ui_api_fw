# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-28 14:59
@Author: guozg 
@File：opera_rely_data.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import json
from jsonpath_rw import parse
import traceback

import sys, os

sys.path.append('../../')

from common.excel.excel_title_mapping import ExcelTitleMapping
from common.util.get_file_path import GetFilePath
from common.util.get_each_dir_abspath import GetEachDirPath
from common.excel.get_excel_cell_value import GetCellValue
from common.method.run_method import RunMethod
from common.request.get_request_data import GetReqData
from common.cookie.opera_cookie import OperaCookie
from common.excel.get_match_data import GetMatchData
from common.config.read_config_data import GetConfigFileData
# # 获取sheet表的名称
# sheetname = GetConfigFileData().get_excel_sheet_name()


class OperaRelyData():
    '''
    操作数据依赖。
    '''

    # def __init__(self, case_id, rely_case_id, sheetname, **kwargs):
    def __init__(self, case_id, rely_case_id, **kwargs):
        '''
        操作数据依赖  \n
        之前是需要传入sheet name，而现在不需要，可以直接读取ini配置即可。
        :param case_id: 当前的case id
        :param rely_case_id: 依赖的caseid
        :param sheetname: sheet表的名称，这个字段将不再进行参数传递，而是直接通过 ini的配置文件进行读取。
        :param kwargs: sheet表的数据,双层dict，外层的dict的key为 caseid；内层dict为每一行的值。
        '''
        self.case_id = case_id
        # 接收传入的依赖的case id
        self.rely_case_id = rely_case_id
        # # 用于读取request的json文件。该文件的名称与sheet表的名称一致。
        # self.sheet_name = sheetname
        # 传入整个sheet表的值，为双层dict
        self.data_dict = kwargs
        # 获取excel表的表头映射
        self.etm = ExcelTitleMapping()

        # 调用所有目录的绝对路径值类
        self.get_each_dir_path = GetEachDirPath()
        # # 拼接request 请求的 json文件路径
        # self.json_file_path = self.get_req_json_file_path()
        # # 获取request请求的json文件中的所有值
        # self.req_data = GetReqData(self.json_file_path)
        # json file path 已经自动获取，不需要进行参数传递。
        self.req_data = GetReqData()
        # # 获取cookie所存放的路径
        # self.cookie_dir = self.get_each_dir_path.get_data_cookie_dir()

    def get_all_rely_case_id(self):
        '''
        获取所有的所依赖的 case id。为一个数组。  \n
        当获取到后，要对该数组进行反转。  \n
        如 login10依赖login08，login08又依赖于login04，login04又依赖于login03，login03依赖于login01  \n
        那么login10 所依赖的所有的case id为['login08','login04','login03','login01']  \n
        但是在执行时，肯定是从login01 开始执行，执行完后，再执行loing03，直到把login08 也执行完  \n
        所以要进行反转，反转后的list为：['login01','login03','login04','login08']
        :return: 反转的list
        '''
        first_rely_case_id = self.rely_case_id
        # # 获取最外层的dict的所有key。该key的值为case id
        # data_dict_keys = self.data_dict.keys()

        # 获取依赖的case id
        rely_case_id = first_rely_case_id

        # 存储所有的依赖的case id
        rely_case_id_list = []
        # 递归。
        while rely_case_id != None:
            rely_case_id_list.append(rely_case_id)
            # 获取所依赖的case所在行的整行数据
            row_data_dict = self.data_dict[rely_case_id]
            # 获取依赖的case id
            rely_case_id = row_data_dict[self.etm.get_rely_case_id()]

        # 进行反转
        case_id_list = rely_case_id_list[::-1]
        # println('反转后的list数据为：',case_id_list)
        # println('原始list数据为：',rely_case_id_list)
        return case_id_list

    def run_all_rely_case(self):
        '''
        运行所有依赖的case  \n
        由于在执行的过程中，上一个依赖的case的请求响应结果会进行相关的数据处理，传递给下一个依赖的case  \n
        所以只需要将最后一个case的执行的响应结果返回即可。  \n
        :return: 返回最后一条用例的执行的响应结果 ->str
        '''
        # 实例化请求类型
        run_method = RunMethod()
        # 获取当前case所依赖的所有的case 为一个list
        rely_case_list = self.get_all_rely_case_id()
        # 所依赖的case 其所在行的整行数据
        row_data_dict = None
        # 用于接收响应结果
        res_tmp = None

        for case_id in rely_case_list:
            # 获取所依赖的case 所在的行的一整行数据
            row_data_dict = self.data_dict[case_id]
            # 实例化获取单元格值对象
            cell_data = GetCellValue(**row_data_dict)
            # 获取相应的数据
            # 获取url
            url = cell_data.get_url()
            # 请求类型
            method = cell_data.get_method()
            # 获取header
            header = cell_data.get_header()
            # 是否保存cookie，当需要保存时，运行该条用例后，要及时的保存
            save_cookie = cell_data.get_save_cookie()
            # 是否有cookie依赖
            rely_cookie_case_id = cell_data.get_rely_cookie_case_id()
            # 获取依赖的响应结果数据对应的字段
            rely_data = cell_data.get_rely_data()
            # 要替换请求数据中哪个字段对应的数据
            rely_req_file = cell_data.get_request_rely_file()
            # 获取请求数据对应json文件中的key
            req_data_key = cell_data.get_requst_data()
            # 获取请求的值
            req_data_dict = self.req_data.get_data(req_data_key)

            if header == 'yes':
                # header的取值 后续再补充
                header = None
            else:
                header = None

            # 给cookie一个默认值为None
            cookie = None
            # 判断是否有cookie依赖
            if rely_cookie_case_id != None:
                cookie = OperaCookie().get_cookie_from_json_file(rely_cookie_case_id)

            # 判断是否从源头开始执行所有的依赖的case
            # 此时可以使用res是否为None 或 rely_data 是否为None进行判断，二者取其一进行判断即可
            # if res == None :
            #     # 表示此时是从源头开始执行
            #     res = run_method.run_main(method,url,req_data_dict,header,cookie)
            #
            # else:
            #     res_tmp = json.loads(res)
            #
            #     jsonpath_expr = parse(rely_data)
            #     find_data = jsonpath_expr.find(res_tmp)
            #     # 获取所依赖的响应结果数据
            #     rely_data_value = [match.value for match in find_data][0]
            #     println('更新前的请求数据为：',req_data_dict)
            #     println('所要替换的key为【 %s 】 对应的响应结果的值为：【 %s 】'%(rely_data,rely_data_value))
            #
            #     # 更新请求数据
            #     req_data_dict[req_data_key] = rely_data_value
            #     println('要替换的key为：',req_data_key)
            #     println('更新后的请求数据：',req_data_dict)
            #
            #     res = run_method.run_main(method,url,req_data_dict,header,cookie)
            print('<p>--- 更新前的请求数据为：', req_data_dict)

            # ===================分割线===========================

            # match_data = GetMatchData(res_tmp,rely_data)
            # # match_res = match_data.get_match_data()
            # rep_req_data = match_data.get_replace_req_data(req_data_dict,rely_req_file)
            #
            # res = run_method.run_main(method, url, rep_req_data, header, cookie)
            # ===================分割线===========================
            '''
            以上几行代码的执行效果与下面几行代码的执行效果一样
            即：将下面几行代码抽取出来，形成公共的方法。
            '''
            # ===================分割线===========================

            if res_tmp != None:
                # 将临时的str响应结果转化为字典，方便查找
                res_tmp_dict = json.loads(res_tmp)

                jsonpath_expr = parse(rely_data)
                find_data = jsonpath_expr.find(res_tmp_dict)
                # 获取所依赖的响应结果数据
                rely_data_value = [match.value for match in find_data][0]
                # 在print()语句里加<p>是为了在BreatifulReport html报告里，能正常的显示为一行数据，否则就会连接在一块，很难查看有用数据

                print('<p>--- 所依赖的数据对应的key为【 %s 】 对应的响应结果的值为：【 %s 】' % (rely_data, rely_data_value))

                # 更新请求数据
                req_data_dict[rely_req_file] = rely_data_value
                print('<p>--- 要替换的key为：', rely_req_file)
                print('<p>--- 更新后的请求数据：', req_data_dict)
                print()

            # println('开始执行请求')
            res = run_method.run_main(method, url, req_data_dict, header, cookie)
            # ===================分割线===========================

            # 将结果转为str类型
            res_tmp = json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=2)
            print('<p>====== -------【 %s 】------响应结果为：-------- ======' % case_id)
            print('<p>',res_tmp)
            print()
            # println(save_cookie)
            # 判断是否要保存cookie
            if save_cookie == 'yes':
                OperaCookie().save_cookie_to_file(case_id, res)

        return res_tmp

    def get_all_rely_data(self):
        '''
        返回当前用例所依赖的case的执行的响应结果  \n
        :return: 所依赖的case的执行的响应结果
        '''
        # 获取当前case所在行的数据
        row_data_dict = self.data_dict[self.case_id]
        # 获取依赖的数据
        rely_data = row_data_dict[self.etm.get_rely_data()]
        print('<p>--- 未处理前的依赖数据为：',rely_data)
        if rely_data == None and rely_data == '':
            rely_data = None
        else:
            try:
                # 获取处理后的响应结果为str类型
                response_value = self.run_all_rely_case()
                print('<p>--- 所获取的响应结果（str）为：',response_value)
                # 将str类型的结果转化为dict
                response_value = json.loads(response_value)
                print('<p>--- 转化后的响应结果（dict）为',response_value)

                jsonpath_expr = parse(rely_data)
                find_data = jsonpath_expr.find(response_value)
                rely_data= [match.value for match in find_data][0]



            except Exception:
                print('<p>--- traceback.format_exc():', traceback.format_exc())
                rely_data = None
        print('<p>--- 最终的返回结果为：',rely_data)
        return rely_data

    # def get_req_json_file_path(self):
    #     '''
    #     获取请求的json对应的request文件路径(含名称)  \n
    #     :return: request 对应的是json文件路径
    #     '''
    #
    #     file_dir = self.get_each_dir_path.get_data_request_dir()
    #     file_name = self.sheet_name
    #     file_path = GetFilePath().get_file_path_json(file_dir, file_name)
    #     return file_path


# excelpath = '../../case/data/interface-data.xlsx'
# sheetname = '105_public_web_login'
# dict_data = ReadExcelData(excelpath, sheetname).get_sheet_data_dict()
# rely_case_id = 'test_login_05'
# case_id = 'test_login_07'
# a = OperaRelyData(case_id,rely_case_id, sheetname,**dict_data)
# println('所依赖的case id为：',a.get_all_rely_case_id())
# println(a.get_all_rely_data())

# help(OperaRelyData)

