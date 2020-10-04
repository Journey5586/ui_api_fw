# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-9-1 22:57
@Author: guozg 
@File：read_config_data.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import sys
import configparser

sys.path.append('../../')
from common.util.get_each_dir_abspath import GetEachDirPath
from common.util.get_file_path import GetFilePath


# __all__ = ['GetConfigFileData']
class GetConfigFileData():
    # ini文件名称
    __file_name = 'run_property.ini'
    # excel节点key
    __node_excel = 'Excel'
    # excel的名称key
    __excel_name = 'excel name'
    # sheet name的key
    __sheet_name = 'sheet name'
    # driver节点 key
    __node_driver = 'Driver'
    # browser的key
    __broswer = 'browser'
    # timeout 的key(这为显示等待超时时间)
    __driver_timeout = 'timeout'
    # implicitly timeout 的key(这为隐式等待超时时间)
    __driver_implicitly_timeout = 'implicitly timeout'
    # 驱动exe 名称对应的key
    __driver_chrome_name = 'chrome driver name'
    __driver_firefox_name = 'firefox driver name'
    __driver_ie_name = 'ie driver name'
    # url
    __url = 'url'
    # 邮件节点的key
    __node_mail = 'Mail'
    # 发件人 key
    __sender = 'sender'
    # 收件人key
    __addressee = 'addressee'
    # 抄送 key
    __cc = 'cc'
    # 邮件主题
    __sub = 'sub'
    # 发件人header key
    __from_header = 'from header'
    # 邮件服务器主机
    __host = 'host'
    # 邮件服务器密码
    __pwd = 'password'
    # 邮件服务端口
    __port = 'port'
    # Request 节点
    __node_request = 'Request'
    # request 的timeout key
    __req_timeout = 'request timeout'
    # report 节点
    __node_report = 'Report'
    # 页面上的报告名称
    __report_title = 'report title'
    # html报告名称
    __report_html_name = 'report html name'
    # 要运行的case的名称的规则 节点
    __node_case_rule = 'CaseRule'
    # case name的指定规则
    __case_name = 'case name rule'

    def __init__(self):
        ''''''
        file_name = self.__file_name
        file_dir = GetEachDirPath().get_config_dir()
        self.config_file_path = GetFilePath().get_file_path_ini(file_dir, file_name)
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path, 'utf-8')

    def get_excel_name(self):
        '''获取excel名称'''
        return self.config.get(self.__node_excel, self.__excel_name)

    def get_excel_sheet_name(self):
        '''获取sheet表的名称'''
        return self.config.get(self.__node_excel, self.__sheet_name)

    def get_driver_browser(self):
        '''
        获取要运行的浏览器，默认值及空值时，均为chrome  \n
        :return: 返回值均为小写
        '''
        browser = str.lower(str.strip(self.config.get(self.__node_driver, self.__broswer)))

        if ('ff' in browser) or ('fire' in browser) or ('firefox' in browser):
            browser = 'firefox'
        elif ('ie' in browser) or ('iexplore' in browser):
            browser = 'ie'
        else:
            browser = 'chrome'

        return browser

    def get_driver_wait_timeout(self) -> int:
        '''
        这是WebDriverWait的超时时间设置,即日常所说的显示等待时间  \n
        获取driver的响应超时 时间设置，默认值为5秒  \n
        当超时设置超过60秒时，最多只为60秒，即最大限制为60秒  \n
        :return: int  [1,60]
        '''
        timeout = self.config.get(self.__node_driver, self.__driver_timeout)
        if timeout == None:
            timeout = 5
        timeout = int(timeout)
        if timeout > 60:
            timeout = 60
        elif timeout < 1:
            timeout = 1

        return timeout

    def get_driver_implicitly_timeout(self) -> int:
        '''
        获取driver的implicitly(隐式)的响应超时时间,该设置为全局设置  \n
        超时时间设置，默认值为5秒  \n
        当超时设置超过60秒时，最多只为60秒，即最大限制为60秒  \n
        :return: int  [5,60]
        '''
        implicitly_timeout = self.config.get(self.__node_driver, self.__driver_implicitly_timeout)
        if implicitly_timeout == None:
            implicitly_timeout = 5
        implicitly_timeout = int(implicitly_timeout)
        if implicitly_timeout > 60:
            implicitly_timeout = 60
        elif implicitly_timeout < 5:
            implicitly_timeout = 5

        return implicitly_timeout

    def get_driver_chrome_exe_name(self):
        '''
        获取chrome的driver exe名称  \n
        :return:
        '''
        chrome_driver = self.config.get(self.__node_driver, self.__driver_chrome_name)
        return chrome_driver

    def get_driver_firefox_exe_name(self):
        '''
        获取firefox的driver exe名称  \n
        :return:
        '''
        firefox_driver = self.config.get(self.__node_driver, self.__driver_firefox_name)
        return firefox_driver

    def get_driver_ie_exe_name(self):
        '''
        获取ie的driver exe名称  \n
        :return:
        '''
        ie_driver = self.config.get(self.__node_driver, self.__driver_ie_name)
        return ie_driver

    def get_url(self):
        '''
        获取url地址  \n
        :return: url
        '''
        url = self.config.get(self.__node_driver, self.__url)
        return url

    def get_mail_sender(self):
        '''邮件的发送者'''
        return self.config.get(self.__node_mail, self.__sender)

    def get_mail_addressee(self):
        '''
        获取邮件的收件人,当有英文的；时表示有多个收件人，要进行切割  \n
        :return: str or list
        '''
        value = self.config.get(self.__node_mail, self.__addressee)
        # 进行判断，是否存在分号，若存在，则表示是多个人
        if ';' in value:
            value = value.split(';')
        return value

    def get_mail_cc(self):
        '''
        获取抄送对象,当有英文；时，表示有多个抄送对象，若为空时，则返回值为None  \n
        :return: None/Str/List
        '''
        value = self.config.get(self.__node_mail, self.__cc)
        if value == '':
            value = None
        elif ';' in value:
            value = value.split(';')

        return value

    def get_mail_sub(self):
        '''
        当邮件主题为空时，会有一个默认值 UI_API_自动化测试报告  \n
        :return:
        '''
        value = str.strip(self.config.get(self.__node_mail, self.__sub))
        if value == '':
            value = 'UI_API_自动化测试报告'
        return value

    def get_mail_from_header(self):
        '''
        给发件人 加标题，在列表里展示发送人就是接口自动化测试  \n
        当为空时，有默认值为：UI_API_自动化测试  \n
        :return: from header的值
        '''
        value = self.config.get(self.__node_mail, self.__from_header)
        if value == '':
            value = 'UI_API_自动化测试'
        return value

    def get_mail_host(self):
        '''获取邮箱服务器主机'''
        return self.config.get(self.__node_mail, self.__host)

    def get_mail_password(self):
        '''获取邮箱服务器的密码'''
        return self.config.get(self.__node_mail, self.__pwd)

    def get_mail_port(self):
        '''获取发送邮件的端口'''
        value = str.strip(self.config.get(self.__node_mail, self.__port))
        if value == '':
            value = None
        return None

    def get_req_timeout(self) -> int:
        '''
        获取request 请求的超时 时间设置，最大时间为30秒，默认为5秒  \n
        :return: int [5,30]
        '''
        timeout = self.config.get(self.__node_request, self.__req_timeout)
        if timeout == None:
            timeout = 5

        timeout = int(timeout)
        if timeout > 30:
            timeout = 30
        elif timeout < 5:
            timeout = 5

        return timeout

    def get_report_title(self):
        '''
        获取页面上的报告的名称(html报告明细页面的报告名称)  \n
        :return: str
        '''
        report_title = self.config.get(self.__node_report, self.__report_title)
        if report_title == '' or report_title == None:
            report_title = '家校平台自动化测试报告明细'
        return report_title

    def get_report_html_name(self):
        '''
        获取发送的html 报告名称  \n
        :return: str
        '''
        html_name = self.config.get(self.__node_report, self.__report_html_name)
        if html_name == '' or html_name == None:
            html_name = 'UI_Api_自动化测试结果'
        return html_name

    def get_case_name_rule(self):
        '''
        获取要运行哪些规则名称的case  \n
        :return: str
        '''
        case_name_rule = self.config.get(self.__node_case_rule, self.__case_name)
        return case_name_rule


# T = GetConfigFileData()
# excel_name = T.get_excel_name()
# println(excel_name, type(excel_name))
# aa = excel_name.split(';')
# println(aa)
# println(T.get_excel_name())
# println(T.get_sheet_name())
# println(T.get_run_browser() == "", type(T.get_run_browser()), '-----', T.get_run_browser())
# println(type(T.get_driver_timeout()),T.get_driver_timeout(),int(T.get_driver_timeout())==30)
# println(T.get_req_timeout())
# println(T.get_excel_name())
# println(T.get_driver_firefox_exe_name())
# println(T.get_url())
# print(T.get_req_timeout())