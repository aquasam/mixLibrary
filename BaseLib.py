# -*- coding: UTF-8 -*-
# Develop by Samuel

#常用请求库
import requests

class BaseReq(object):

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "Content- Type": "application/x-www-form-urlencoded",
        }

    def get(self, url, cookie=None, **kwargs):
        # 创建GET请求，加入伪装和cookie(str)
        if cookie:
            cookies = {'cookie': cookie}
            self.headers = dict(self.headers, **cookies)
        response = requests.get(url=url, headers=self.headers, **kwargs)
        return response

    def post(self, url, data, cookie, **kwargs):
        # 创建POST请求，加入伪装和cookie(str)
        if cookie:
            cookies = {'cookie': cookie}
            self.headers = dict(self.headers, **cookies)
        response = requests.post(url=url, data=data, headers=self.headers, **kwargs)
        return response



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

class BaseSe(object):

    def init_browser(self, headless=True):
        # 初始化chrome浏览器，提供选择可见或不可见模式
        if not headless:
            browser = webdriver.Chrome()
        else:
            driver_options = Options()
            driver_options.add_argument('--headless')
            browser = webdriver.Chrome(chrome_options=driver_options)
        return browser

    def cookie_form(self, browser, Fjson=True):
        # 通过selenium获取cookie，并将cookie转换为string 或者 dict
        cookie_list = browser.get_cookies()
        cookie_dict = {}
        for cookie in cookie_list:
            cookie_dict[cookie['name']] = cookie['value']
        sum = []
        for key in cookie_dict:
            sum.append(key + '=' + cookie_dict[key] + ';')
        cookies = ''.join(list(sum))[:-1]
        browser.close()
        cookies = '\"{cookie:\'%s\'}\"'%cookies
        if not Fjson:
            cookies = json.loads(cookies)
        return cookies


#常用html分析库
import re
from lxml import etree

class BaseParse(object):
    def re_parse(self):
        pass

    def etee_parse(self):
        pass


#常用log库
        #   使用例：
        #   log = BaseLog(name, path)
        #   self.logger = log.Clog(self.__class__.__name__)
import logging
from time import localtime, time, strftime
class BaseLog(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.logLevel = logging.DEBUG
        self.asFile = True
        self.asConsole = True

    def Clog(self, funcName):

        formatter = logging.Formatter('%(asctime)s - %(name)s/%(funcName)s [%(levelname)s] : %(message)s')

        logger = logging.getLogger(funcName)
        logger.setLevel(level=self.logLevel)

        # 生成文件名
        currentTime = strftime('%Y%m%d%H%M', localtime(time()))
        fileName = self.name + currentTime
        # 确认路径下是否存在该目录
        bos = BaseOS()
        bos.check_file(self.path, createPath=True)
        location = os.path.join(self.path, fileName)
        # 设置保存日志内容
        if self.asFile:
            handler = logging.FileHandler(location)
            handler.setLevel(level=self.logLevel)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        # 设置输入日志内容
        if self.asConsole:
            console = logging.StreamHandler()
            console.setLevel(level=self.logLevel)
            console.setFormatter(formatter)
            logger.addHandler(console)

        return logger


#常用文件处理库

class BaseOS(object):

    def check_file(self, path, createPath=True):
        # 检查目标文件是否存在,存在返回True,不存在返回False
        if not os.path.exists(path):
            if os.path.exists(os.path.dirname(path)):
                print('已存在目录：{}'.format(os.path.dirname(path)))
            else:
                print('未存在目标目录：{}'.format(os.path.dirname(path)))
                if createPath:
                    os.makedirs(os.path.dirname(path))
                    print('已创建目录：{}'.format(os.path.dirname(path)))
            return False
        else:
            print('已存在文件：{}'.format(path))
            return True

    def delete_file(self, path):
        #删除目标文件或文件夹
        self.check_file(path, createPath=False)
        if os.path.isfile(path):
            os.remove(path)
        else:
            os.removedirs(path)



class BaseFile(BaseOS):

    def read_file(self, path):
        if super().check_file(path=path, createPath=False):
            with open(path, "r") as f:
                data = f.readlines()
            return data

    def save_file(self, path, data):
        if not super().check_file(path=path, createPath=True):

            with open(path, 'w') as f:
                if type(data) == list:
                    for da in data:
                        f.write(str(da)+'\n')
                elif type(data) == str:
                    f.write(data)


import xlrd
import xlwt
from xlutils import copy
import os

class BaseXL(BaseOS):
    def __init__(self, path):
        self.path = path

    #* * * * * * * * 数据写入xls文件* * * * * * * *
    def initXL(self, sheet=[]):
        # 初始化表格，生成指定sheet
        workbook = xlwt.Workbook(encoding='utf=8')
        for sh in sheet:
            workbook.add_sheet(sh, cell_overwrite_ok=True)
        return workbook

    def set_size(self, sheet, col, row, width, height):
        # 设置指定行，列宽高
        sheet.col(col).width = width
        sheet.row(row).set_style(xlwt.easyxf('font:height {};'.format(height)))

    def save_as_xls(self, workbook):
        # 保存xls文件
        if not super().check_file(path=self.path, createPath=True):
            workbook.save(self.path)
            print('已生成{}'.format(os.path.basename(self.path)))

    #* * * * * * * * 读取xls文件* * * * * * * * *

    def openXL(self, sheet):
        if super().check_file(path=self.path, createPath=False):
            workbook = xlrd.open_workbook()
            return workbook
        else:
            print('未找到指定文件：{}'.format(self.path))


if __name__ == '__main__':
    test =BaseOS()
    test.delete_file('test/test1.txt')
