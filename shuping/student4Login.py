#coding=utf-8

import os
import unittest

#from BeautifulReport import BeautifulReport
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from common.commonConfig import CommonConfig
import configparser


def getPath(self):
    try:
        root_path = os.path.dirname(os.path.abspath('.') + '/config/chromedriver/chromedriver')
        return root_path
        print("Config root_path=" + root_path)
    except:
        print("获取path失败!")


def getUrl(TypeUrl, urlName):
    try:
        config = configparser.ConfigParser()
        urlconfig = os.path.dirname(os.path.abspath('.') + '/config/config.ini/config.ini')
        config.read(urlconfig)
        url = config.get(TypeUrl, urlName)
        print("Config url=" + url)
    except:
        print("获取url失败!")
    return url

# class student4TestCase(unittest.TestCase):
#
#     def test_case1_Login(self):
#        '''学生端登录'''
        #try:
path = os.path.dirname(os.path.abspath('.') + '/config/chromedriver/chromedriver')
print("path:" + path)
# linux路径
# path = "/usr/local/python3/chromedriver"
url = getUrl("TypeUrl", "student4Url")
print("url:" + url)

# linux使用的静默执行方法
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')

# 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
# options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/Default')
# linux配置
# driver = webdriver.Chrome(executable_path=path, chrome_options=options)
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(20)
driver.get(url)
driver.maximize_window()
print(u"\nLogin start!")

driver.find_element_by_xpath("//span[@class='ant-select-arrow']").click()
driver.find_element_by_xpath(
    "//ul[@class='ant-select-dropdown-menu ant-select-dropdown-menu-vertical  ant-select-dropdown-menu-root']/li[1]").click()
driver.find_element_by_id("username").send_keys("18400000000")
driver.find_element_by_id("password").send_keys("000000")
# 点击登录按钮
driver.find_element_by_xpath("//button[@type='submit']").click()
print("Login Success!")
username = driver.find_element_by_class_name("userName").text

#except:
#print("登录失败")
assert("测试学生1", username)
driver.close()
driver.quit()


# testsuite = unittest.TestSuite()
# testsuite.addTests(unittest.makeSuite(student4TestCase))
# reportpath = os.path.dirname(os.path.abspath('.') + '/report/report')
# run = BeautifulReport(testsuite)
# run.report(filename='学生端测试报告.html', description='学生端测试用例', report_dir=reportpath)

# if __name__ == "__main__":
#     s = student4TestCase()
#     s.test_case1_Login()
    #unittest.main
    #student4TestCase.test_Login()
