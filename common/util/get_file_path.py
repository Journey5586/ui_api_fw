# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-29 11:37
@Author: guozg 
@File：get_file_path.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import os


class GetFilePath():
    '''拼接文件路径'''

    def get_file_path_xlsx(self, filedir, filename):
        '''拼接excel格式的文件路径'''
        file_dir = filedir
        file_name = filename
        file_name = file_name if file_name.endswith('.xlsx') or file_name.endswith('.xlx') else file_name + '.xlsx'
        file_path = os.path.abspath(os.path.join(file_dir, file_name))
        return file_path

    def get_file_path_json(self, filedir, filename):
        '''拼接json格式的文件路径'''
        file_dir = filedir
        file_name = filename
        file_name = file_name if file_name.endswith('.json') else file_name + '.json'
        file_path = os.path.abspath(os.path.join(file_dir, file_name))
        return file_path

    def get_file_path_html(self, filedir, filename):
        '''拼接html格式的文件路径'''
        file_dir = filedir
        file_name = filename
        file_name = file_name if file_name.endswith('.html') else file_name + '.html'
        file_path = os.path.abspath(os.path.join(file_dir, file_name))
        return file_path

    def get_file_path_ini(self, filedir, filename):
        '''拼接ini格式的文件路径'''
        file_dir = filedir
        file_name = filename
        file_name = file_name if file_name.endswith('.ini') else file_name + '.ini'
        file_path = os.path.abspath(os.path.join(file_dir, file_name))
        return file_path

    def get_file_path_log(self,filedir,filename):
        '''拼接log格式的文件路径'''
        file_dir = filedir
        file_name = filename
        file_name = file_name if file_name.endswith('.log') else file_name + '.log'
        file_path = os.path.abspath(os.path.join(file_dir, file_name))
        return file_path

    def get_file_path_exe(self,filedir,filename):
        '''拼接exe格式的文件路径'''
        file_dir = filedir
        file_name = filename
        file_name = file_name if file_name.endswith('.exe') else file_name + '.exe'
        file_path = os.path.abspath(os.path.join(file_dir, file_name))
        return file_path

    def get_file_path_png(self,filedir,filename):
        '''拼接png格式的文件路径'''
        file_dir = filedir
        file_name = filename
        file_name = file_name if file_name.endswith('.png') else file_name + '.png'
        file_path = os.path.abspath(os.path.join(file_dir, file_name))
        return file_path

# help(GetFilePath)