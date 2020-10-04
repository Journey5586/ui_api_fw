# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-11-01 9:26
@Author: guozg 
@File：file_upload.py
@Description: 
1.文件上传，针对的是点击上传按钮，然后弹出windows的选择文件窗口，选择文件，然后进行上传
2.本类主要是针对上传文件不在 upload_file目录下。
@Modify Time:  
@Modify Description: 
1.
2.
"""
import os
from common.util.get_upload_file_path import GetUploadFilePath

class FileUpload():
    '''
    文件上传，针对的是点击上传按钮，然后弹出windows的选择文件窗口，选择文件，然后进行上传  \n
    本类主要是针对上传文件不在 upload_file目录下。 \n
    当然也可上传 upload_file目录下的文件  \n

    '''
    def __init__(self,files_path):
        '''
        实例化时，要传入要上传文件的路径(含文件名称)，当有多个文件时，文件名称之间用分号";"分隔开  \n
        如：d:\\infox.txt;d:\\info01.txt;d:\\info02.txt  \n
        需要注意的是 文件的路径之间必须是双斜杠，即为 d:\\info.txt，而不是 d:\info.txt  \n
        防止斜杠后面跟一些字母 如 t 将字母进行转义了，如 \t 就会进行转义  \n
        :param files_path: 要上传文件的路径(含文件名称)，如 d:\\infox.txt;d:\\info01.txt;d:\\info02.txt
        '''
        self.__fpath = files_path
        # 是否是多个文件标识变量
        self.__flag = 0
        # 先判断是否有多个文件，检测是否包含了";"
        if ';' in self.__fpath :
            self.__fpath = self.__fpath.split(';')
            self.__flag = 1

    def get_files(self):
        '''
        获取所有文件，当所有的文件均在同一个目录下，则要对文件的显示方式进行整合，将这些文件一次性进行上传  \n
        如果在不同目录下，则需要进行for循环，依次进行上传 \n
        一次性上传的显示方式为："d:\\infox.txt" "d:\\info01.txt" "d:\\info02.txt"  \n
        如果是list 如['d:\\infox.txt', 'd:\\info01.txt', 'd:\\info02.txt']则表示要进行多次上传  \n
        :return: str or list
        '''
        files = ""
        flag = self.__check_dir_is_same()
        if flag == False:
            files = self.__fpath
        else :
            tmp = ""
            space = ' '
            count = len(self.__fpath)
            for i in range(count):
                tmp= self.__fpath[i]
                if i <count-1:
                    files =files+ '"'+tmp+'"'+space
                elif i == count -1:
                    files = files +'"'+tmp+'"'

        return files

    def get_files_list(self):
        '''
        不在对上传的文件是否为同一个目录下，进行校验，直接将传入的文件切割成每一份单独的文件，  \n
        此时为list，然后在实际上传时，要进行 for循环 进行上传  \n
        :return: list 如：['d:\\infox.txt', 'd:\\\info01.txt', 'd:\\info02.txt']
        '''
        return self.__fpath

    def __check_dir_is_same(self):
        '''
        检测批量上传的文件是否均在同一个目录下。如果在同一个目录下，则要将数据进行改造  \n
        返回的数据为：'"d:\\infox.txt" "d:\\info01.txt" "d:\\info02.txt"'  \n
        如果不在同个目录下，则不对切割后的list数据进行任何的加工，直接返回list
        :return: bool
        '''
        # 设置标识变量
        flag = None
        tmp_flag = 0
        # 当self.__flag为0时，表示只上传一个文件，不需要进行任何的切割或加工
        if self.__flag == 0:
            flag = False
        # 表示要上传多个文件
        else :
            '''
            取出list中的第一个数据，然后获取目录，再依次的跟如下的数据的目录进行对比
            当和余下的数据的目录全部都一样时，则表示此次上传的文件均在同一个目录下，
            此时要进行数据改造；否则表示有不同目录下的文件。不再进行加工处理。
            '''
            count = len(self.__fpath)
            first_file = self.__fpath[0]
            first_file_dir = os.path.split(first_file)[0]

            for i in range(1,count):
                file = self.__fpath[i]
                # 获取文件的路径目录
                file_dir = os.path.split(file)[0]

                if first_file_dir == file_dir :
                    tmp_flag +=1

            if tmp_flag == (count -1):
                # 表示第一个文件所在的目录跟余下的所有文件的目录均一样。
                flag = True
            else :
                flag = False

        # 返回最终的标识
        return flag

    def get_imgs_urls(img_urls):
        '''
        处理文件绝对路径格式，以便使用sendkeys可以同时上传多个文件
        :return: 多个字符串 如：'d:\\infox.txt'\n'd:\\\info01.txt'\n'd:\\info02.txt'
        '''
        img_real_url = GetUploadFilePath(img_urls).get_files_path()  # 获取附件完整地址
        sendkeys_urls = img_real_url.replace(" ", "\n").replace('"', "")  # 格式化地址，处理成sendkeys可以识别的地址
        return sendkeys_urls

# help(FileUpload)