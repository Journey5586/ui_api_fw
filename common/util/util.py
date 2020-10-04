# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-11-19 20:41
@Author: guozg 
@File：util.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import re


class Util():

    def getNumOfStr(self, strNum: str) -> str:
        """
        使用正则过滤掉字符串的非数字字符，返回数字，类型为str
        :param strNum: 要过滤非数字字符的字符串
        :return: 过滤后的数字，类型为str。如果是从页面上获取的值，是需要转化为encode("utf8")
        """
        # 使用正则替换掉所有的非数字字符
        str_num = re.sub("\D", "", strNum)
        return str_num

    def calcPageCount(self, rec_count: int, pagesize=10) -> int:
        """
        计算总共有多少页，即总页数。要传入总记录条数，每页展示的条数。
        :param rec_count:总记录数
        :param pagesize:每页展示的记录数，默认为10条
        :return:计算出的总页数
        """
        """
        在python3.0之前，如果两个整数相除，得到的结果仍然为整数，若有一个数为浮点数时，则结果为浮点数
        例：1/2 为0，1.0/2 为0.5
        所以在计算的时候有两种方法，一种为将传入的str转换为float类型，
        一种为转化为int类型，但是在进行判断大小的时候，必须要判断余数是否为0。
        建议使用 将str转换为float类型，然后再对返回值转换为int类型
        """
        # 直接进行类型转换，不再进行strip 去空格操作
        # # 方法一：
        # rec_count_ = int(rec_count)
        # pagesize_ = int(pagesize)
        # pagecount_tmp1 = rec_count_ // pagesize_
        # pagecount_tmp2 = rec_count_ / pagesize_
        # pagecount_tmp3 = rec_count_ % pagesize_
        # # 计算真正的总页数
        # if (pagecount_tmp1 == pagecount_tmp2) and pagecount_tmp3 == 0:
        #     pagecount = pagecount_tmp1
        # else:
        #     pagecount = pagecount_tmp1 + 1
        # return pagecount

        # 方法二
        rec_count_ = float(rec_count)
        pagesize_ = float(pagesize)
        pagecount_tmp1 = rec_count_ // pagesize_
        pagecount_tmp2 = rec_count_ / pagesize_
        if (pagecount_tmp1 == pagecount_tmp2):
            pagecount = pagecount_tmp1
        elif pagecount_tmp2 > pagecount_tmp1:
            pagecount = pagecount_tmp1 + 1
        return int(pagecount)

    # def expandTree(self, driver, locator):
    #     """
    #     传入浏览器驱动，及定位器。其中定位器locator为一个元组tuple
    #     具体写法如 locator = (By.CLASSNAME,"starttime0")
    #     :param driver:浏览器驱动
    #     :param locator:定位器，其值为元组(By.CLASSNAME,"starttime0")
    #     :return:无任何结果返回。
    #     """
    #     driver_ = driver
    #     locator_ = locator
    #     trees = _find_elements(driver_, locator_)
    #     count = len(trees)
    #     # 进行递归循环点击+号 展开树
    #     while count > 0:
    #         for i in range(count):
    #             trees[i].click()
    #
    #         # 当将当前的+号全部点击完后，再进行一次重新获取
    #         sleep(5)
    #         trees = _find_elements(driver_, locator_)
    #         count = len(trees)
    #
    # def _find_element(driver, by):
    #     """
    #     私有函数，浏览器驱动，定位器(元组)
    #     :param driver: 浏览器驱动
    #     :param by: 定位器，如：(By.CLASSNAME,"starttime")
    #     :return: 返回定位到的元素
    #     """
    #     try:
    #         return driver.find_element(*by)
    #     except NoSuchElementException as e:
    #         # raise e
    #         return False
    #     except WebDriverException as e:
    #         raise e
    #
    # def _find_elements(driver, by):
    #     """
    #     私有方法，浏览器驱动，定位器(元组)
    #     :param driver: 浏览器驱动
    #     :param by: 定位器，如(By.CLASSNAME,"startname")
    #     :return: 返回一个列表。
    #     """
    #     try:
    #         return driver.find_elements(*by)
    #     except WebDriverException as e:
    #         raise e


# help(Util)