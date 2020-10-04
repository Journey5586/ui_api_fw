# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-11-06 19:41
@Author: guozg 
@File：get_upload_file_path.py
@Description: 
1.本类主要是解决从upload_file 文件夹下上传文件
2.将传入的文件拼接上upload_file的路径
@Modify Time:  
@Modify Description: 
1.
2.
"""
import sys
import os

sys.path.append('../../')
from common.util.get_each_dir_abspath import GetEachDirPath as dirpath


class GetUploadFilePath():
    '''
    1.本类主要是解决从upload_file 文件夹下上传文件  \n
    2.将传入的文件拼接上upload_file的路径  \n
    '''

    def __init__(self, files_name):
        '''
        实例化时，要传入要上传文件的文件名称，当有多个文件时，文件名称之间用分号";"分隔开  \n
        如：infox.txt;info01.txt;info02.txt  \n
        注：调用此类，表示所有文件均存在于upload_file 目录下，要从upload_file目录下，对这些文件进行上传操作  \n
        :param files_name: 文件名称，如“infox.txt;info01.txt;info02.txt”，或“infox.txt”
        '''
        self.__files = files_name
        self.__flag = 0
        # 先判断是否有多个文件，检测是否包含了";"
        if ';' in self.__files:
            self.__files = self.__files.split(';')
            self.__flag = 1

    def get_files_path(self):
        '''
        对传入的文件名称，拼接相应的路径  \n
        当有多个文件时，返回的值为  \n
        '"I:\\py3_autotest\\zhjx\\upload_file\\infox.txt" "I:\\py3_autotest\\zhjx\\upload_file\\info01.txt"'  \n
        当有一个文件时，返回的值为'd:\\upload_file\\infox.txt'  \n
        :return: str
        '''

        files = ''
        file_path = ''
        file_dir = dirpath().get_upload_file_dir()
        if self.__flag == 0:
            files = os.path.abspath(os.path.join(file_dir, self.__files))
        else:
            tmp = ''
            space = ' '
            # file_dir = dirpath().get_upload_file_dir()
            count = len(self.__files)
            for i in range(count):
                tmp = self.__files[i]
                # 若文件的名称里已经包括了 upload_file的目录，则下面的拼接后的结果仍然正确
                file_path = os.path.abspath(os.path.join(file_dir, tmp))
                if i < count - 1:
                    files = files + '"' + file_path + '"' + space
                elif i == count - 1:
                    files = files + '"' + file_path + '"'

        return files

# if __name__ == '__main__':
#     aa = 'infox.txt;info01.txt;info02.txt'
#     fp = GetUploadFilePath(aa)
#     println(fp.get_files_path())
# help(GetUploadFilePath)