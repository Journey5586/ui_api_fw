# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2019-08-16 8:55
@Author: 郭志国 
@File：base_web.py
@Description: 
1. PO 或 POM 模式的 base文件，基本够用了。
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import traceback
# 鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
# 键盘事件
from selenium.webdriver.common.keys import Keys
# 传统的下拉列表select
from selenium.webdriver.support.select import Select


from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By
# 导入键盘操作 针对是的 window对话框的操作，非浏览器页面上的键盘操作。
from pykeyboard import PyKeyboard

import sys
import time

sys.path.append('../')
from common.config.read_config_data import GetConfigFileData
from common.util.get_time import GetTime
from common.util.get_file_path import GetFilePath
from common.util.get_each_dir_abspath import GetEachDirPath
from common.util.output_msg_to_html import Output

cur_time = GetTime().get_cur_time()

config = GetConfigFileData()
# 获取显示等待时间
timeout = config.get_driver_wait_timeout()
# 获取隐式等待时间
implicitly_timeout = config.get_driver_implicitly_timeout()
'''
初始化 driver的代码必须 写成为一个公共的方法，在外部传入到base里，否则会出问题
当一个py文件里，来回的登录、退出、登录、退出…… 等操作时，如果 driver写到 base文件里，
此时每当登录一次，都会多出一个driver，这是不合理的。
所以将driver的初始化工作放在外面，传入到base文件里。
下面注释的代码为 driver相关的代码。
web端的 driver 公共方法为 common.config.init_web_driver.init_driver()
'''
# browser = config.get_driver_browser()
# chrome_driver_exe = config.get_driver_chrome_exe_name()
# firefox_driver_exe = config.get_driver_firefox_exe_name()
# ie_driver_exe = config.get_driver_ie_exe_name()

url = config.get_url()

# driver_log_dir = GetEachDirPath().get_driver_log_dir()
# driver_dir = GetEachDirPath().get_driver_dir()
# # 设置浏览器驱动exe的路径
# chrome_exe_path = GetFilePath().get_file_path_exe(driver_dir, chrome_driver_exe)
# firefox_exe_path = GetFilePath().get_file_path_exe(driver_dir, firefox_driver_exe)
# ie_exe_path = GetFilePath().get_file_path_exe(driver_dir, ie_driver_exe)
# # 设置各浏览器驱动输出的log名称
# chrome_log_name = 'chrome_log' + cur_time
# firefox_log_name = 'firefox_log' + cur_time
# ie_log_name = 'ie_log' + cur_time
# # 设置各浏览器的log路径
# chrome_log_path = GetFilePath().get_file_path_log(driver_log_dir, chrome_log_name)
# firefox_log_path = GetFilePath().get_file_path_log(driver_log_dir, firefox_log_name)
# ie_log_path = GetFilePath().get_file_path_log(driver_log_dir, ie_log_name)

HTML_IMG_TEMPLATE = """【{}】--双击/右键新标签页看大图:<img src="data:image/png;base64, {}" width="400px" height="225px" style="border:1px solid blue" onclick="show_img(this)"/>"""
img_dir = GetEachDirPath().get_img_dir()


class BaseWeb():
    ''''''

    # def __init__(self, __driver, url):
    #     # 运行代码时，下一行代码要注释掉
    #     # __driver = webdriver.Chrome()
    #     self.__driver = __driver
    #     self.__url = url
    #     self.__timeout = timeout
    #     self.__driver.implicitly_wait(5)
    #     # self.open_url()

    # def __init__(self, driver = None):
    #     ''''''
    #     self.driver = self.__get_driver()
    #     self.__url = url
    #     self.__timeout = timeout
    #     self.driver.implicitly_wait(5)
    #     # self.open_url()

    def __init__(self, driver: webdriver):
        self.__url = url
        self.driver = driver
        self.__timeout = timeout
        self.__implicitly_timeout = implicitly_timeout
        self.driver.implicitly_wait(self.__implicitly_timeout)
        self.__output = Output()

    '''
    初始化 driver的代码必须 写成为一个公共的方法，在外部传入到base里，否则会出问题
    当一个py文件里，来回的登录、退出、登录、退出…… 等操作时，如果 driver写到 base文件里，
    此时每当登录一次，都会多出一个driver，这是不合理的。
    所以将driver的初始化工作放在外面，传入到base文件里。
    下面注释的代码为 driver相关的代码。
    web端的 driver 公共方法为 common.config.init_web_driver.init_driver()
    __get_driver()私有方法被弃用。
    '''

    # def __get_driver(self):
    #     if browser == 'ie':
    #         driver = webdriver.Ie(executable_path=ie_exe_path, log_level='WARNING', log_file=ie_log_path)
    #     elif browser == 'firefox':
    #         driver = webdriver.Firefox(executable_path=firefox_exe_path, log_path=firefox_log_path)
    #     else:
    #         driver = webdriver.Chrome(executable_path=chrome_exe_path, service_log_path=chrome_log_path)
    #
    #     return driver

    def driver_quit(self):
        '''退出driver'''
        self.driver.quit()

    def page_close(self):
        '''
        当只有一个tab页时，关闭当前浏览器  \n
        当有多个tab页时，关闭的是当前tab页  \n
        :return: None
        '''
        # # 方法一 使用此方法 有可能会导致当脚本失败或错误时，无法自动截图
        self.driver.close()
        # # 方法二，使用 Ctrl + w 快捷键，关闭tab页，chrome与firefox均支持.在linux里要将ctrl换成alt
        # # 该方法在执行的时候，不友好，有时候会没有反应，并没有执行
        # ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()

    def maximize_window(self):
        '''窗口最大化'''
        self.driver.maximize_window()

    def open_url(self):
        '''打开url'''
        self.maximize_window()
        self.driver.get(self.__url)
        # print(self.driver.get_window_size())
        # print(self.get_all_tabs())
        # print(self.driver.page_source)

    def set_window_size(self, width: int, height: int):
        '''设置窗口大小'''
        self.driver.set_window_size(width, height)

    def refresh_page(self):
        '''刷新页面'''
        self.driver.refresh()

    def get_page_source(self):
        '''获取并返回页面的资源'''
        return self.driver.page_source

    def switch_to_frame(self, frame_id):
        '''
        切入到frame中  \n
        :param frame_id: frame 的id
        :return: None
        '''
        self.driver.switch_to.frame(frame_id)

    def switch_to_default_content(self):
        '''切入到最外层页面中'''
        self.driver.switch_to.default_content()

    def get_all_tabs(self) -> list:
        '''
        获取当前浏览器中所有打开的tab页在内存中的handle  \n
        注：  \n
        selenium打开浏览器后，如果打开页面上的链接时，会自动打开一个新的tab页。  \n
        当打开多个tab页后， 需要注意以下两点：  \n
        默认的主页面为未打开新tab页时的那个tab页，即浏览器上的第一个tab页(下标为0)  \n
        其余的tab页的序号和打开的先后成倒序排列。  \n
        即最先打开的tab页排序最后面，下标序号也就越大；最后打开的tab页排在最前面，序号也就越小  \n
        最后打开的那个tab页的序号为1 \n
        :return: list(tab页的handle)
        '''
        handles = self.driver.window_handles
        # print(handles)
        return handles

    def switch_to_default_tab(self):
        '''
        切换到默认的tab页，或者是主页面。  \n
        :return: 切换到默认的主页面
        '''
        handles = self.get_all_tabs()
        # print(handles)
        # print(handles[0])
        self.driver.switch_to.window(handles[0])

    def get_all_tabs_titile(self) -> dict:
        '''
        获取所有的tab页的title，并存入到dict中 返回  \n
        :return: dict{tab_index:tab_title}
        '''
        handles = self.get_all_tabs()
        # 获取当前的tab
        current_tab = self.driver.current_window_handle
        title_dict = {}
        count = len(handles)
        for i in range(count):
            self.driver.switch_to.window(handles[i])
            title = self.driver.title
            title_dict[i] = title

        # 再切回到当前的tab页
        self.driver.switch_to.window(current_tab)

        return title_dict

    def switch_tabs_by_title(self, title_name):
        '''
        根据tab页的title进行切换到目标tab页  \n
        :param title_name: tab页的title名称
        :return: None
        '''
        handles = self.get_all_tabs()
        title = title_name

        '''
        方法一 的实现思想与方法二 一致。方法二执行的效率可能更高一些。
        '''

        # 方法一
        title_dict = self.get_all_tabs_titile()
        for key, item in title_dict.items():
            if title in item:
                self.driver.switch_to.window(handles[key])

        # # 方法二
        # tabs_count = len(handles)
        # flag = 0
        # cur_tab = self.driver.current_window_handle
        # for i in range(tabs_count):
        #     self.driver.switch_to.window(handles[i])
        #     # 获取当前页面的title
        #     page_titile = self.driver.title
        #     if title in page_titile:
        #         flag = 1
        #         break
        #     else:
        #         pass
        # # 判断是否查找到目标tab页
        # if flag == 0:
        #     # 当未查找到目标tab页时，是需要切回之前的当前页的。
        #     self.driver.switch_to.window(cur_tab)

    def switch_tabs_by_index(self, index: int):
        '''
        传入目标tab页的索引，从0开始  \n
        :param index: 目标tab页的索引
        :return: None
        '''
        handles = self.get_all_tabs()
        self.driver.switch_to.window(handles[index])

    def save_browser_img(self, img_name):
        """
        保存图片，需要传入驱动、图片路径、图片名称  \n
        # :param driver: 驱动
        :param img_name: 图片名称
        :return: None
        """
        driver = self.driver
        img_name = img_name if img_name.endswith('.png') else img_name + '.png'
        img_path = GetFilePath().get_file_path_png(img_dir, img_name)

        try:
            driver.get_screenshot_as_file(img_path)
        except Exception as msg:
            # print(msg)
            self.__output.str_msg(msg)
            pass

    def save_img_to_html_base64(self, img_name):
        """
        保存图片为base64，存放于htmlreport 中   \n
        # :param driver: 驱动
        :param img_name: 图片名称
        :return: None
        """
        try:
            # 获取driver属性对象
            driver = self.driver
            # 进行截图 base64
            img = driver.get_screenshot_as_base64()
            img_name = img_name if img_name.endswith('.png') else img_name + '.png'
            # print(HTML_IMG_TEMPLATE.format(img_name, img))
            self.__output.str_msg(HTML_IMG_TEMPLATE.format(img_name, img))

        except Exception as msg:
            msg = "【传入的不是driver】,因为：【{}】,所以【无法进行base64截图】".format(msg)
            # print(msg)
            self.__output.str_msg(msg)
            pass

    def find_element(self, locator: tuple):
        '''
        查找元素，返回查找到的元素  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: element
        '''
        flag = self.__locator_is_tuple(locator)

        if flag == True:

            try:

                ele = WebDriverWait(self.driver, self.__timeout).until(EC.visibility_of_element_located(locator))
                return ele
            except Exception as msg:
                self.__print_msg(locator)
                self.__print_detail_msg()

        elif flag == False:
            self.__print_msg(locator)

        # 当为None时，错误信息已经输出过了
        else:
            pass

    def find_elements(self, locator: tuple):
        '''
        查找一组属性相同的元素，返回是个list  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: list
        '''
        flag = self.__locator_is_tuple(locator)
        if flag == True:

            try:
                eles = WebDriverWait(self.driver, self.__timeout).until(
                    EC.visibility_of_all_elements_located(locator))
                return eles
            except Exception as msg:
                self.__print_msg(locator)
                self.__print_detail_msg()

        elif flag == False:
            self.__print_msg(locator)

        # 当为None时，错误信息已经输出过了
        else:
            pass

    def select_by_visible_text(self, locator, text_value: str):
        '''
        通过下拉列表里可见的文本进行选择  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :param text_value: 下拉列表中的值，如每页显示50条,必须为str类型，不能是数字
        :return: None
        '''
        ele = self.find_element(locator)
        try:
            Select(ele).select_by_visible_text(text_value)
        except Exception:
            # print('你输入的列表值【 %s 】不存在' % text_value)
            self.__output.str_msg('你输入的列表值【 %s 】不存在' % text_value)
            self.__print_detail_msg()

    def ele_is_exist(self, locator: tuple):
        '''
        检查元素是否存在，存在则返回该元素，不存在则返回false  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: element or false
        '''
        flag = self.__locator_is_tuple(locator)

        if flag == True:

            try:

                ele = WebDriverWait(self.driver, self.__timeout).until(EC.visibility_of_element_located(locator))
                return ele
            except Exception as msg:
                self.__print_msg(locator)
                self.__print_detail_msg()
                return False

        elif flag == False:
            self.__print_msg(locator)
            return False

        # 当为None时，错误信息已经输出过了
        else:
            return False

    def ele_is_selected(self, locator: tuple):
        '''
        判断单选框或复选框是否被选中  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: bool or None
        '''

        try:
            is_selected = self.find_element(locator).is_selected()
            if is_selected:
                return True
            else:
                return False

        except Exception as msg:
            self.__print_msg(locator)
            self.__print_detail_msg()
            return None

    def send_keys(self, locator: tuple, key_value):
        '''
        向文本框输入值,其中locator为元组  \n
        在输入数据之前，要先清空已有的值  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :param key_value: 要输入的值
        :return: None
        '''
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(key_value)

    def send_keys_by_element(self,webelement:webelement,key_value):
        '''向目标元素对象的文本框输入值'''
        webelement.send_keys(key_value)

    def click(self, locator: tuple):
        '''
        元素的点击操作  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: None
        '''
        ele = self.find_element(locator)
        ele.click()

    def click_by_element(self,webelement:webelement):
        '''目标元素的点击操作'''
        webelement.click()


    def clear_input(self, locator: tuple):
        '''
        清空文本框输入的内容  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: None
        '''
        ele = self.find_element(locator)
        ele.clear

    def alert_accept(self):
        '''
        点击alert弹窗的确定按钮  \n
        :return: None
        '''
        alert = self.alert_is_present()
        if alert != None:
            alert.accept()
        else:
            self.__alert_error_print()

    def alert_dismiss(self):
        '''
        点击alert弹窗的取消按钮  \n
        :return: None
        '''
        alert = self.alert_is_present()
        if alert != None:
            alert.dismiss()
        else:
            self.__alert_error_print()

    def alert_is_present(self):
        '''
        检测alert是否出现  \n
        :return: 检测到的alert 对象 or None
        '''
        time.sleep(2)
        alert = None
        try:
            alert = self.driver.switch_to.alert
            alert.text
            return alert
        except Exception:
            # self.__alert_error_print()
            self.__print_detail_msg()
            alert = None
        finally:
            return alert

    def get_alert_msg(self):
        '''
        获取去掉 回车换行符后的提示信息。  \n
        :return:  text ->str
        '''
        return self.format_alert_msg()

    def format_alert_msg(self):
        '''
        去掉alert弹窗提示信息中的 回车换行，即完整的获取提示信息  \n
        :return: 去掉回车换行符后的提示信息。
        '''
        alert = self.alert_is_present()
        if alert != None:
            msg = alert.text
            # 检测是否有 回车或换行
            if '\r' in msg or '\n' in msg:
                msg = msg.replace('\r', '').replace('\n', '')
            return msg
        else:
            return None

    # def switch_to_frame(self, frame_name):
    #     '''
    #     切入到frame中  \n
    #     :param frame_name: frame的名称
    #     :return: None
    #     '''
    #     self.driver.switch_to.frame(frame_name)
    #
    # def switch_out_frame(self):
    #     '''
    #     切出frame  \n
    #     :return: None
    #     '''
    #     self.driver.switch_to.default_content()

    def js_remove_readonly(self, attr_value, attr_name='ById'):
        '''
        执行js脚本，移除元素的只读属性  \n
        例：js_remove_readonly("askforleave_date","ByName")   \n
        :param attr_value: 属性值，如askforleave_date
        :param attr_name: 属性名，为ByClassName,ByTagName,ByName,ById,ByTagNameNS 5种中的4种,其中ByTagNameNS本该当不支持。
        :return: None
        '''
        # 获取元素的属性名
        attr_name = attr_name
        # 进行去空格及小写转化
        attr_name = str.lower(str.strip(attr_name))
        attr_value = str.strip(attr_value)
        after_js = '")[0].removeAttribute("readonly")'
        after_js_id = '").removeAttribute("readonly")'
        # 进行判断
        if 'classname' in attr_name:
            before_js = 'document.getElementsByClassName("'

        elif 'tagname' in attr_name:
            before_js = 'document.getElementsByTagName("'

        elif 'byname' in attr_name:
            before_js = 'document.getElementsByName("'

        elif 'id' in attr_name:
            before_js = 'document.getElementById("'

        # 拼接js脚本
        if 'ById' in before_js:
            js = before_js + attr_value + after_js_id
        else:
            js = before_js + attr_value + after_js

        # 执行js脚本
        # self.driver.execute_script(js)
        self.execute_script(js)

    def js_add_readonly(self, attr_value, attr_name='ById'):
        '''
        执行js脚本，移除元素的只读属性  \n
        例：js_add_readonly("askforleave_date","ByName")   \n
        :param attr_value: 属性值，如askforleave_date
        :param attr_name: 属性名，为ByClassName,ByTagName,ByName,ById,ByTagNameNS 5种中的4种,其中ByTagNameNS本该当不支持。
        :return: None
        '''
        # 获取元素的属性名
        attr_name = attr_name
        # 进行去空格及小写转化
        attr_name = str.lower(str.strip(attr_name))
        attr_value = str.strip(attr_value)
        after_js = '")[0].setAttribute("readonly","True")'
        after_js_id = '").setAttribute("readonly","True")'

        # 进行判断
        if 'classname' in attr_name:
            before_js = 'document.getElementsByClassName("'

        elif 'tagname' in attr_name:
            before_js = 'document.getElementsByTagName("'

        elif 'byname' in attr_name:
            before_js = 'document.getElementsByName("'

        elif 'id' in attr_name:
            before_js = 'document.getElementById("'

        # 拼接js脚本
        if 'ById' in before_js:
            js = before_js + attr_value + after_js_id
        else:
            js = before_js + attr_value + after_js

        # 执行js脚本
        # self.driver.execute_script(js)
        self.execute_script(js)

    def execute_script(self, js):
        '''
        直接执行javascript脚本，如退出 logout()  \n
        :param js: javacript脚本，如logout()
        :return: None
        '''
        # println('调用 退出脚本')
        self.driver.execute_script(js)

    def right_click(self, locator: tuple):
        '''
        在目标元素对象上的进行右键  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: None
        '''
        ele = self.find_element(locator)
        ActionChains(self.driver).context_click(ele).perform()

    def double_click(self, locator: tuple):
        '''
        在目标元素对象上进行双击操作  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: None
        '''
        ele = self.find_element(locator)
        ActionChains(self.driver).double_click(ele).perform()

    def mouse_over(self, locator: tuple):
        '''
        在目标元素对象上进行悬停   \n
        :param locator: 定位器，类型为tuple，如(By.ID,"username")
        :return: None
        '''
        ele = self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def key_ENTER(self, locator: tuple):
        '''
        向目标元素输入enter键  \n
        :param locator: 目标元素定位器，tuple类型，如(By.ID,'username')
        :return: None
        '''
        self.send_keys(locator, Keys.ENTER)

    def key_BACKSPACE(self, locator: tuple):
        '''
        向目标元素输入BACKSPACE键  \n
        :param locator: 目标元素定位器，tuple类型，如(By.ID,'username')
        :return: None
        '''
        self.send_keys(locator, Keys.BACKSPACE)

    def key_TAB(self, locator):
        '''
        Tab键  \n
        :param locator: 目标元素定位器，tuple类型，如(By.ID,'username')
        :return: None
        '''
        self.send_keys(locator, Keys.TAB)

    def key_COPY(self, locator: tuple):
        '''
        拷贝  \n
        :param locator: 目标元素定位器，tuple类型，如(By.ID,'username')
        :return: None
        '''
        self.send_keys(locator, (Keys.CONTROL, 'c'))

    def key_PASTE(self, locator: tuple):
        '''
        粘贴  \n
        :param locator: 目标元素定位器，tuple类型，如(By.ID,'username')
        :return: None
        '''
        self.send_keys(locator, (Keys.CONTROL, 'v'))

    def key_CUT(self, locator: tuple):
        '''
        剪切  \n
        :param locator: 目标元素定位器，tuple类型，如(By.ID,'username')
        :return: None
        '''
        self.send_keys(locator, (Keys.CONTROL, 'x'))

    def key_SELECTALL(self, locator: tuple):
        '''
        全选  \n
        :param locator: 目标元素定位器，tuple类型，如(By.ID,'username')
        :return: None
        '''
        self.send_keys(locator, (Keys.CONTROL, 'a'))

    def key_ESC(self, locator: tuple):
        '''
        取消  \n
        :param locator: 目标元素定位器，tuple类型，如(By.ID,'username')
        :return: None
        '''
        self.send_keys(locator, Keys.ESCAPE)

    def windialog_upload(self, files):
        '''
        window 对话框 上传文件  \n
        :param files: 要上传的文件，请先调整common.util.fileupload.FileUpload()类 对文件进行加工，将加工后的结果传入进来。 \n
        :return: None
        '''
        keyboard = PyKeyboard()
        keyboard.type_string(files)
        keyboard.tap_key(keyboard.enter_key)
        # time.sleep(5)

    def __alert_error_print(self):
        '''
        当未检测到alert弹窗时，在控制台窗口的输出信息  \n
        :return: None
        '''
        msg = '----未检测到alert弹窗！！！----'
        # print(msg)
        self.__output.str_msg(msg)

    def __locator_is_tuple(self, locator: tuple):
        '''
        判断传入的定位器locator的类型是否为tuple，如果不是,则不进行元素定位 \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: bool True、False、None(异常时)
        '''
        flag = None

        try:
            if (isinstance(locator, tuple)):
                flag = True
            else:
                flag = False
        except Exception as msg:
            self.__print_msg(locator)
            self.__print_detail_msg()
            flag = None
        finally:
            return flag

    def __print_msg(self, locator: tuple):
        '''
        输出错误信息  \n
        :param locator: 定位器，类型为tuple,如(By.ID,"username")
        :return: None
        '''
        # print("输入的定位器无效：", locator)
        # self.__output.str_msg(("输入的定位器无效：", locator))
        self.__output.str_msg("输入的定位器无效：")
        self.__output.str_msg(locator)

    def __print_detail_msg(self):
        '''
        输出详情的错误信息  \n
        :return: None
        '''
        # print('traceback.format_exc():', traceback.format_exc())
        # self.__output.str_msg(('traceback.format_exc():', traceback.format_exc()))
        self.__output.str_msg('traceback.format_exc():')
        self.__output.str_msg(traceback.format_exc())

# help(BaseWeb)