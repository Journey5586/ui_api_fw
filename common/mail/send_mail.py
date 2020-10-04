# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-30 10:02
@Author: guozg 
@File：send_mail.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""

# 导入邮件服务
import smtplib
# 导入邮件格式
from email.mime.text import MIMEText
from email.header import Header
# 在邮件里添加附件
from email.mime.multipart import MIMEMultipart
import os
import traceback
import sys

sys.path.append('../../')
from common.config.read_config_data import GetConfigFileData


class SendMail():
    """
    发送邮件，可以上传多个附件。
    """
    # 发件人
    global sender
    # 发送服务器的地址
    global host
    # 邮箱登录密码
    global password

    def __send_mail(self, content, file_path, cc=None):
        """
        发送邮件的主体  \n
        :param receiver: 收件人 可以是一个list
        :param sub: 主题
        :param content: 内容
        :param file_path: 要上传的附件，可以上传一个或多个
        :return:
        """
        __from = 'From'
        __to = 'To'
        __cc = 'Cc'
        __subject = 'Subject'
        mail_conf_data = GetConfigFileData()
        # 发件人
        sender = mail_conf_data.get_mail_sender()

        # 收件人
        addressee = mail_conf_data.get_mail_addressee()
        # 抄送
        cc = mail_conf_data.get_mail_cc()

        # 邮件服务器地址
        host = mail_conf_data.get_mail_host()
        # 邮箱登录密码
        password = mail_conf_data.get_mail_password()
        # 获取邮件主题
        sub = mail_conf_data.get_mail_sub()
        # 获取发件人标题
        from_header = mail_conf_data.get_mail_from_header()

        # 创建一个带附件的实例
        message = MIMEMultipart()

        # 给发件人 加标题，在列表里展示发送人就是接口自动化测试
        message[__from] = Header(from_header, "utf-8")
        # 收件人
        # 要判断是str还是list
        if isinstance(addressee, str):
            message[__to] = addressee
        elif isinstance(addressee, list):
            message[__to] = ";".join(addressee)
        # 抄送
        # 判断抄送对象是str还是list
        if isinstance(cc, str):
            message[__cc] = cc
        elif isinstance(cc, list):
            message[__cc] = ";".join(cc)

        # 邮件主题
        message[__subject] = Header(sub, "utf-8")

        # # 邮件正文内容 文本格式
        # message.attach(MIMEText(content, _subtype="plain", _charset="utf-8"))
        # 邮件正文内容 html格式
        message.attach(MIMEText(content, _subtype="html", _charset="utf-8"))
        file_path = file_path
        '''
        在此处要判断是str还是tuple
        当为str时，表示要上传一个附件
        当为tuple，表示要上传多个附件
        '''
        if file_path == None:
            print("不上传附件")
            pass
        elif isinstance(file_path, str):
            file_path = str.strip(file_path)
            if file_path == "":
                print("附件为空，不进行上传附件操作")
                pass
            else:
                file_path = os.path.abspath(file_path)
                # 获取文件名
                filename = os.path.split(file_path)[-1]

                # 构造附件1，上传../../data/interface-data.xlsx 文件
                att1 = MIMEText(open(file_path, "rb").read(), "base64", _charset="utf-8")
                att1["Content-Type"] = "application/octet-stream"
                """
                # 这里的filename可以任意写，写的名称将在邮件的附件中展示什么样的名称
                # 这里需要注意的是：附件名称必须是双引号，否则发送的邮件附件将不能正确展示
                # 同时需要注意的是：附件必须带后缀，必须与上传的附件的类型要保持一致，否则会乱码
                由于filename有以上这些问题，所以将自动获取filename
                """

                # att1["Content-Disposition"] = 'attachment;filename="' + filename + '"'
                # 下面两行代码均可以解决附件名称有中文，发送后显示为bin文件的问题。建议使用第二种,第一种会出现乱码的情况
                # att1.add_header('Content-Disposition', 'attachment', filename=filename)
                att1.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename))
                message.attach(att1)
        elif isinstance(file_path, tuple) or isinstance(file_path, list):
            for file in file_path:
                att = None
                # 获取文件名
                filename = os.path.split(file)[-1]
                # 构造附件1，上传../../data/interface-data.xlsx 文件
                att = MIMEText(open(file, "rb").read(), "base64", "utf-8")
                att["Content-Type"] = "application/octet-stream"
                """
                # 这里的filename可以任意写，写的名称将在邮件的附件中展示什么样的名称
                # 这里需要注意的是：附件名称必须是双引号，否则发送的邮件附件将不能正确展示
                # 同时需要注意的是：附件必须带后缀，必须与上传的附件的类型要保持一致，否则会乱码
                由于filename有以上这些问题，所以将自动获取filename
                """
                # att["Content-Disposition"] = 'attachment;filename="' + filename + '"'
                # 下面两行代码均可以解决附件名称有中文，在接收附件时，显示为bin的名称。建议使用第二种，第一种会出现乱码的情况
                # att.add_header('Content-Disposition', 'attachment', filename=filename)
                att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename))
                message.attach(att)

        try:
            # 邮件服务器
            server = smtplib.SMTP()
            # 连接服务器
            server.connect(host)
            # 登录邮箱
            server.login(sender, password)
            # 发送邮件
            server.sendmail(sender, addressee, message.as_string())
            # # 关闭
            # server.quit()
            # server.close()
            print("邮件发送成功！！！")
            # return True
        except Exception as msg:
            print("邮件发送失败，错误信息如下：")
            print(msg)
            print("具体的错误详细信息如下：")
            print('traceback.format_exc():', traceback.format_exc())
            # return False
        finally:
            # 关闭
            server.quit()
            server.close()

    def send_main(self, pass_list, fail_list, err_list, skip_list, file_path):
        """
        发送邮件的正文,有附近，如果不想上传附件，则file_path = “” 或file_path=None 即可  \n
        该方法适用于自己写的框架，不使用unittest框架  \n
        :param pass_list: 通过的case的list(该list记录的是case所在的行号)
        :param fail_list: 失败的case的list(该list记录的是case所在的行号)
        :param err_list: 失败的case的list(该list记录的是case所在的行号)
        :param skip_list: 失败的case的list(该list记录的是case所在的行号)
        :param file_path: 发送的附件,可以str 也可以是tuple或list。当为tuple/list时，将添加多个附件
        :return:
        """
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        err_num = float(len(err_list))
        skip_num = float(len(skip_list))
        count_num = pass_num + err_num + skip_num + fail_num
        sub = "接口自动化测试报告"
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        err_result = "%.2f%%" % (err_num / count_num * 100)
        skip_result = "%.2f%%" % (skip_num / count_num * 100)

        # 发送html 格式的邮件
        content_html = """
        <p>Hi All!</p>
        <p>1：此次一共运行了接口测试用例【{}】个 </p>
        <p>2：通过的个数为【{}】条，通过率为【{}】</p>
        <p>3：失败的个数为【{}】条，失败率为【{}】</p>
        <p>4：发生错误的个数为【{}】条，错误率为【{}】</p>
        <p>5：跳过的个数为【{}】条，跳过率为【{}】</p>
        """.format(int(count_num), int(pass_num), pass_result, int(fail_num), fail_result, int(err_num), err_result,
                   int(skip_num), skip_result)

        # 进行邮件发送
        self.__send_mail(content_html, file_path)

    def send_main_rpt(self, pass_count, fail_count, err_count, skip_count, att_file_path):
        """
        发送邮件的正文,有附近，如果不想上传附件，则file_path = “” 或file_path=None 即可  \n
        该方法适用于使用unititest框架，有html报告的。  \n
        :param pass_count: 通过的case的个数
        :param fail_count: 失败的case的个数
        :param err_count: 失败的case的个数
        :param skip_count: 失败的case的个数
        :param att_file_path: 发送的附件,可以str 也可以是tuple或list。当为tuple/list时，将添加多个附件
        :return:
        """
        pass_num = float(pass_count)
        fail_num = float(fail_count)
        err_num = float(err_count)
        skip_num = float(skip_count)
        count_num = pass_num + err_num + skip_num + fail_num
        sub = "接口自动化测试报告"
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        err_result = "%.2f%%" % (err_num / count_num * 100)
        skip_result = "%.2f%%" % (skip_num / count_num * 100)

        # 发送html 格式的邮件
        content_html = """
        <p>Hi All!</p>
        <p>1：此次一共运行了接口测试用例【{}】个 </p>
        <p>2：通过的个数为【{}】条，通过率为【{}】</p>
        <p>3：失败的个数为【{}】条，失败率为【{}】</p>
        <p>4：发生错误的个数为【{}】条，错误率为【{}】</p>
        <p>5：跳过的个数为【{}】条，跳过率为【{}】</p>
        """.format(int(count_num), int(pass_num), pass_result, int(fail_num), fail_result, int(err_num), err_result,
                   int(skip_num), skip_result)

        # 进行邮件发送
        self.__send_mail(content_html, att_file_path)



# help(SendMail)