# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-09-04 16:39
@Author: guozg 
@File：save_screenshot.py
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
from common.util.get_each_dir_abspath import GetEachDirPath
from common.util.get_file_path import GetFilePath

img_dir = GetEachDirPath().get_img_dir()

HTML_IMG_TEMPLATE = """【{}】--双击/右键新标签页看大图:<img src="data:image/png;base64, {}" width="400px" height="225px" style="border:1px solid blue" onclick="show_img(this)"/>"""


class SaveScreenShot():
    '''进行截图 base64 直接保存到html中 或 保存为png格式，直接存放于 img目录下'''

    def save_browser_img(self, driver, img_name):
        """
        保存图片，需要传入驱动、图片路径、图片名称  \n
        :param driver: 驱动
        :param img_name: 图片名称
        :return: None
        """
        driver = driver
        img_name = img_name if img_name.endswith('.png') else img_name + '.png'
        img_path = GetFilePath().get_file_path_png(img_dir, img_name)

        try:
            # driver.get_screenshot_as_file('{}/{}'.format(img_dir, img_name))
            driver.get_screenshot_as_file(img_path)
        except Exception as msg:
            print(msg)
            pass

    def save_img_to_html_base64(self, driver, img_name):
        """
        保存图片为base64，存放于htmlreport 中   \n
        :param driver: 驱动
        :param img_name: 图片名称
        :return: None
        """
        try:
            # 获取driver属性对象
            driver = driver
            # 进行截图 base64
            img = driver.get_screenshot_as_base64()
            img_name = img_name if img_name.endswith('.png') else img_name + '.png'
            print(HTML_IMG_TEMPLATE.format(img_name, img))

        except Exception as msg:
            msg = "【传入的不是driver】,因为：【{}】,所以【无法进行base64截图】".format(msg)
            print(msg)
            pass


# help(SaveScreenShot)