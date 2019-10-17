# -*- coding:utf-8 -*-

import os
from common.commonConfig import CommonConfig
import time
import unittest
import ApiTest
import conMysql
from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.common.by import By

from BeautifulReport import BeautifulReport

#from selenium.webdriver.support import expected_conditions as EC


class Teacher4TestCase(unittest.TestCase):


    def setUp(self):
        try:
            global driver
            # mac
            path = CommonConfig.getPath(self)
            # linux路径
            #path = "/usr/local/python3/chromedriver"
            url = CommonConfig.getUrl("TypeUrl", "teacherxUrl")

            # linux使用的静默执行方法
            # options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # options.add_argument('--no-sandbox')

            # 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
            #options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/Default')
            # linux配置
            # driver = webdriver.Chrome(executable_path=path, chrome_options=options)
            driver = webdriver.Chrome(executable_path=path)
            driver.implicitly_wait(20)
            driver.get(url)
            driver.maximize_window()
            print(u"\nLogin start!")
            driver.find_element_by_xpath("//span[@class='ant-select-arrow']").click()
            driver.find_element_by_xpath("//ul[@class='ant-select-dropdown-menu ant-select-dropdown-menu-vertical  ant-select-dropdown-menu-root']/li[1]").click()
            driver.find_element_by_id("username").send_keys("18817572035")
            driver.find_element_by_id("code").send_keys("1111")
            #点击登录按钮
            driver.find_element_by_xpath("//button[@type='submit']").click()
            #Log.info("setp_login ending...")
            print("Login Success!")
        except :
            print("登录失败")

    def tearDown(self):
        try:
            driver.close()
        except:
            print("close fail")


    def click(self, loc):
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located(By.XPATH, loc))
            return True
        except:
            print(u'元素点击失败！')
            #self.saveScreenShot_error('元素点击失败')
            return False

    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        # mac存放图片路径
        driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"/Users/shuping/Python_code/SeleniumTest/img"), img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        # mac存放图片路径2
        #driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"/Users/shuping/.jenkins/workspace/autotest/img"), img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        # linux存放图片路径
        #driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"/usr/local/python3/img"), img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径

    # 判断元素是否存在的方法
    def isElementExist(self, element):
        flag = True
        try:
            # locator2 = (By.XPATH, element)
            # WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator2))
            driver.implicitly_wait(5)
            if driver.find_element_by_xpath(element):
                return flag
        except:
            flag = False
            return flag

    def isElementExistclass(self, element):
        flag = True
        try:
            if driver.find_element_by_class_name(element):
                return flag
        except:
            flag = False
            return flag

    @BeautifulReport.add_test_img('test_1_right')
    def test_1_right(self):
        '''招生测评英语五年级——做对'''
        testperson=""
        try:
            #  登录后点击招生测评模块
            driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div/div[2]/div[6]").click()
            # 点击立即分享
            driver.find_element_by_xpath(
                "//*[@id='root']/div/div/main/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/span[1]").click()
            # window_1 = driver.window_handles
            # window_2 = driver.current_window_handle
            time.sleep(1)
            # turl = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[3]/div[2]/a/span").text
            turl = driver.find_element_by_xpath("//div[@class='img-url']/a/span").text
            newwindow = "window.open(\"" + turl + "\");"
            # js = 'window.open("https://shupingorg.t1.learnta.cn/teacher4");'
            driver.execute_script(newwindow)
            window1 = driver.window_handles
            # 跳转到新标签页
            driver.switch_to.window(window1[1])
            time.sleep(1)
            # 输入姓名
            # driver.find_element_by_name("username").send_keys("测试招生测评_复制链接")
            driver.find_element_by_xpath("//form[@class='cSign__form']/div[1]/input").send_keys("测试招生测评_复制链接")
            # 输入手机号
            driver.find_element_by_xpath("//form[@class='cSign__form']/div[2]/input").send_keys("18817572035")
            # driver.find_element_by_name("mobile").send_keys("18817572035")
            # 输入验证码
            driver.find_element_by_xpath("//form[@class='cSign__form']/div[3]/input").send_keys("1111")
            # driver.find_element_by_name("code").send_keys("1111")
            # 点击选择地区下拉框
            driver.find_element_by_xpath("//span[@class='ant-cascader-picker']").click()
            # driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[4]/span/input").click()
            # 点击选择天津（省）
            driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[1]/li[2]").click()
            # driver.find_element_by_xpath("/body/div[3]/div/div/div/ul[1]/li[2]").click()
            # 选择天津市
            driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[2]/li[1]").click()
            # 选择和平区
            driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[3]/li[1]").click()
            # 再点击一次筛选地区筛选框
            driver.find_element_by_xpath("//div[@class='recTitle']").click()
            # js = "var q=document.getElementByclassName('pMainCon').scrollTop=0"
            # driver.execute_script(js)
            # 滚动页面的滚动条
            driver.execute_script("window.scrollBy(0,100)")
            # 点击登录，开始测评
            driver.find_element_by_xpath("//form[@class='cSign__form']/a/span").click()
            time.sleep(0.5)
            name = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/ul/li[1]").text
            # 点击开始测评
            driver.find_element_by_xpath("//div[@class='step step-1']/ul/li[1]").click()
            # 选择英语
            driver.find_element_by_xpath("//div[@class='step step-1']/ul/li[1]").click()
            # driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/ul/li[1]").click()
            # 点击五年级
            driver.find_element_by_xpath("//div[@class='step step-2']/ul/li[2]").click()
            # 循环点击专题下一题按钮
            elementflag = self.isElementExist("//div[@class='btnWrapper']/a[2]")
            # elementflag = self.isElementExist("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]")
            while (elementflag):
                time.sleep(0.5)
                proquestionId = ApiTest.ApiTest.test_get_01(self)
                qlist = ApiTest.ApiTest.test_post_01(self, proquestionId)
                # 如果是选择题
                if qlist[1] == 0:
                    # 查询题目的答案
                    answer_2 = conMysql.ConnMysql.testOption(self, qlist[0])
                    if answer_2 == "A":
                        driver.find_element_by_xpath(
                            "//*[@id='root']/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li[1]").click()
                        # 点击下一题按钮
                        driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
                    elif answer_2 == "B":
                        driver.find_element_by_xpath(
                            "//*[@id='root']/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li[2]").click()
                        # 点击下一题按钮
                        driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
                    elif answer_2 == "C":
                        driver.find_element_by_xpath(
                            "//*[@id='root']/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li[3]").click()
                        # 点击下一题按钮
                        driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
                    elif answer_2 == "D":
                        driver.find_element_by_xpath(
                            "//*[@id='root']/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li[4]").click()
                        # 点击下一题按钮
                        driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
                elif qlist[1] == 1:  # 如果是填空题
                    answerblank = conMysql.ConnMysql.test_blank(self, qlist[0])
                    inputlist = driver.find_elements_by_xpath("//input[@class='gapInput']")
                    for i in range(len(inputlist)):
                        inputlist[i].send_keys(answerblank[i])
                    # 点击下一题按钮
                    driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
                    # 点击弹窗的确定按钮
                elementflag = self.isElementExist("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]")

            reportname = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div[2]/p[2]").text
            print("测评报告：", reportname)
            testperson = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div[1]/p").text
            print("测试人：", testperson)

            score = driver.find_element_by_xpath("//*[@id='analyzeReport']/div/div[1]/div[1]/p[2]").text
            print("得分：", score)
        except:
            print("test allright fail!")
        self.assertEqual("ceshi", testperson)

    @BeautifulReport.add_test_img('test_2_wrong')
    def test_2_wrong(self):
        '''招生测评英语五年级——全做错'''
        testperson=""
        try:
            # 登录后点击招生测评模块
            # driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[3]/div[3]/div[2]").click()
            driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div/div[2]/div[6]").click()

            # 点击登录后的招生测评
            # driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[3]/div[2]").click()
            time.sleep(1)
            # 点击立即分享
            driver.find_element_by_xpath(
                "//*[@id='root']/div/div/main/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/span[1]").click()
            time.sleep(1)
            # window_1 = driver.window_handles
            # window_2 = driver.current_window_handle
            turl = driver.find_element_by_xpath("//div[@class='img-url']/a/span").text
            newwindow = "window.open(\"" + turl + "\");"
            driver.execute_script(newwindow)
            window1 = driver.window_handles
            # 跳转到新标签页
            driver.switch_to.window(window1[1])
            time.sleep(1)
            # 输入姓名
            driver.find_element_by_name("username").send_keys("测试招生测评_复制链接")
            # 输入手机号
            driver.find_element_by_name("mobile").send_keys("18817572035")
            # 输入验证码
            driver.find_element_by_name("code").send_keys("1111")
            # 点击选择地区下拉框
            driver.find_element_by_xpath("//span[@class='ant-cascader-picker']").click()
            # 点击选择天津（省）
            driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[1]/li[2]").click()
            # 选择天津市
            driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[2]/li[1]").click()
            # 选择和平区
            driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[3]/li[1]").click()
            # 再点击一次筛选地区筛选框
            driver.find_element_by_xpath("//div[@class='recTitle']").click()
            # 滚动页面的滚动条
            driver.execute_script("window.scrollBy(0,100)")
            # 点击登录，开始测评
            driver.find_element_by_xpath("//form/a/span").click()
            time.sleep(1)
            name = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/ul/li[1]").text
            # 点击开始测评
            driver.find_element_by_xpath("//div[@class='step step-1']/ul/li[1]").click()
            # 选择英语
            driver.find_element_by_xpath("//div[@class='step step-1']/ul/li[1]").click()
            # 点击五年级
            driver.find_element_by_xpath("//div[@class='step step-2']/ul/li[2]").click()

            # 循环点击专题下一题按钮
            elementflag = self.isElementExist("//div[@class='btnWrapper']/a[2]")
            while (elementflag):
                driver.find_element_by_xpath("//div[@class='btnWrapper']/a[2]").click()
                time.sleep(0.5)
                # 点击弹窗的确定按钮
                driver.find_element_by_xpath("//div[@class='ant-confirm-btns']/button[2]").click()
                time.sleep(0.5)
                # 下一题按钮是否存在
                elementflag = self.isElementExist("//div[@class='btnWrapper']/a[2]")

            reportname = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div[2]/p[2]").text
            print("测评报告：", reportname)
            testperson = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div[1]/p").text
            print("测试人：", testperson)
            score = driver.find_element_by_xpath("//*[@id='analyzeReport']/div/div[1]/div[1]/p[2]").text
            print("得分：", score)
            # self.assertEqual("测评报告", reportname)
        except:
            print("test wrong fail")
        self.assertEqual("ceshi", testperson)
        driver.close()
        driver.quit()

    # @BeautifulReport.add_test_img('test_c_creatCourse')
    # def test_c_creatCourse(self):
    #     '''创建课程'''
    #     now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    #     courseName = ""
    #     ResultcourseName = ""
    #     try:
    #         print("Create course start !")
    #         time.sleep(1)
    #         #进入主页的备课系统按钮
    #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
    #         time.sleep(1)
    #         # 点击创建课程按钮
    #         driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-lg pullRight createBtn noCopyBtn']").click()
    #         time.sleep(1)
    #         #点击选择数学
    #         driver.find_element_by_xpath("//form/div[1]/div[2]/div/div/label[2]").click()
    #         #点击选择沪教版
    #         driver.find_element_by_xpath("//form/div[2]/div[2]/div/div/label[5]").click()
    #         time.sleep(1)
    #         #点击输入课程名称
    #         courseName = "自动化测试课程" + now
    #         driver.find_element_by_xpath("//*[@id='courseName']").send_keys(courseName)
    #         # 点击确定按钮
    #         driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
    #         # 点击选择年级下拉框按钮
    #         driver.find_element_by_xpath("//div[@class='wrapper selectWrapper wrapper-default']/span").click()
    #         # 点击五年级
    #         driver.find_element_by_xpath("//div[@class='ant-cascader-menus ant-cascader-menus-placement-bottomLeft']/div/ul[1]/li[5]").click()
    #         # 点击选择五年级上
    #         driver.find_element_by_xpath("//div[@class='ant-cascader-menus ant-cascader-menus-placement-bottomLeft']/div/ul[2]/li[1]").click()
    #         time.sleep(1)
    #         # 点击添加单元按钮
    #         driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-ghost ant-btn-lg addButton']").click()
    #         time.sleep(1)
    #         # 点击选择新的单元
    #         driver.find_element_by_xpath("//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical  ant-dropdown-menu-light ant-dropdown-menu-root']/li[2]").click()
    #         print("  Add unit success ...")
    #         # 点击添加教学点模块下拉框
    #         driver.find_element_by_xpath("//div[@class='Course']/div[3]/div/div[3]/div[2]/button").click()
    #         time.sleep(1)
    #         # 点击选择教学点模块
    #         driver.find_element_by_link_text("教学点模块").click()
    #         time.sleep(1)
    #         print("  Add jiaoxuedian success ...")
    #         #点击选择教学点下拉框
    #         driver.find_element_by_xpath("//div[@class='ant-modal-body']/span").click()
    #         # 点击八年级上册下拉按钮
    #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/span").click()
    #         #点击第十一章三角形下拉按钮
    #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/ul/li[1]/span").click()
    #         # 点击11.1按钮
    #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/ul/li[1]/ul/li[1]/span").click()
    #         # 点选择 11.1.1
    #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/ul/li[1]/ul/li[1]/ul/li[1]/span").click()
    #         time.sleep(1)
    #         # 点击选择三角形的三边关系（可选）
    #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/ul/li[1]/ul/li[1]/ul/li[1]/ul/li/a/span").click()
    #         time.sleep(1)
    #         # 点击确定按钮
    #         driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
    #         # 创建完课程取课程名字
    #         ResultcourseName = driver.find_element_by_class_name("headerTitle").text
    #         print("Create course success! ")
    #     except:
    #         print("Create course failed!")
    #     self.assertEqual(courseName, ResultcourseName, msg="创建课程失败!")
    #
    # @BeautifulReport.add_test_img('test_d_IntelligenceCard')
    # def test_d_IntelligenceCard(self):
    #     '''创建智能练习卡 '''
    #     #driver = driver
    # #   kk = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("kw"), message="worry!")
    #     cardName=""
    #     try:
    #         # 进入主页的备课系统按钮
    #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
    #         # 点击课程
    #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
    #         #time.sleep(1)
    #         # 设置等待添加按钮时间后点击按钮
    #         # locator2 = (By.XPATH, "//button[@class='ant-card lTaskCard lTaskCard-type-add ant-card-bordered']")
    #         # WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator2))
    #         # 点击添加按钮
    #         driver.find_element_by_xpath("//div[@class='lCourseUnitStep']/div/div[last()]/div").click()
    #         time.sleep(1)
    #         # 点击添加智能练习卡按钮
    #         driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[5]/a").click()
    #         time.sleep(1)
    #         # 点击创建按钮
    #         driver.find_element_by_xpath("//button[@type='submit']").click()
    #         #time.sleep(1)
    #         print("  Add intelligenceCard success ...")
    #         # 创建完课程取课程名字
    #         #courseName = driver.find_element_by_class_name("headerTitle").text
    #         cardName = driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div[1]/div/div/div/div[5]/div/div/div/div/div[2]").text
    #         print("Create intelligenceCard success!")
    #     except:
    #         print("Create intelligenceCard error!")
    #     self.assertEqual("二次根式的概念", cardName, msg="创建智能练习卡失败！")
    #
    # @BeautifulReport.add_test_img('test_e_textcard')
    # def test_e_textcard(self):
    #     '''创建富文本卡'''
    #     card_name=""
    #     try:
    #         # page = driver.page_source  #获取源码
    #         # doc = pq(page)
    #         # doc = etree.HTML(str(doc))
    #         # contents = doc.xpath('//div[@class="ant-card-body"]/div[1]/div/div/div')
    #         #
    #         # for x in contents:
    #         #     x.xpath("/div[5]/div")
    #         # 进入主页的备课系统按钮
    #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
    #         # 点击课程
    #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
    #         # 点击教学点模块
    #         driver.find_element_by_xpath("//div[@class='ant-card-body']/div[2]/button").click()
    #         #driver.find_element_by_link_text("教学点模块").click()
    #         # 点击教学活动
    #         driver.find_element_by_link_text("教学活动").click()
    #         #driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li[2]").click()
    #         time.sleep(1)
    #         # 点击添加任务卡按钮
    #         driver.find_element_by_xpath("//div[@class='courseUnitSteps']/div[2]/div/div/div/div/div").click()
    #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div[1]/div[2]/div/div/div/div").click()
    #         time.sleep(1)
    #         # 点击选择富文本卡按钮
    #         driver.find_element_by_xpath("//div[@class='ant-card lTaskCard lTaskCard-type-rich_text ant-card-bordered']/div").click()
    #         #driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/div/div/a/div").click()
    #
    #         driver.find_element_by_id("taskName").send_keys("测试富文本卡")
    #         time.sleep(0.5)
    #         # 点击react-box获取焦点
    #         driver.find_element_by_xpath("//div[@class='ant-row ant-form-item introductionFormItem']/div[2]/div/div/div/div[2]").click()
    #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[3]/div[2]/div/div/div").click()
    #         # 输入备注文本
    #         driver.find_element_by_xpath("//div[@class='ant-row ant-form-item introductionFormItem']/div[2]/div/div/div/div[2]").send_keys("测试添加备注内容")
    #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[3]/div[2]/div/div/div/div[2]").send_keys("测试添加备注内容")
    #         time.sleep(0.5)
    #         # 获取任务描述的焦点
    #         driver.find_element_by_xpath("//div[@class='ant-row ant-form-item taskDataFormItem']/div[2]/div/div/div[1]/div/div[2]").click()
    #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[4]/div[2]/div/div/div").click()
    #         # 输入任务描述的文本
    #         driver.find_element_by_xpath("//div[@class='ant-row ant-form-item taskDataFormItem']/div[2]/div/div/div[1]/div/div[2]").send_keys("测试添加富文本卡任务描述内容")
    #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[4]/div[2]/div/div/div/div[2]").send_keys("测试添加富文本卡任务描述内容")
    #         time.sleep(0.5)
    #         # 点击创建按钮
    #         driver.find_element_by_xpath("//button[@class ='ant-btn ant-btn-primary ant-btn-lg']").click()
    #         card_name=driver.find_element_by_xpath("//div[@class='courseUnitSteps']/div[2]/div/div/div[1]/div//div/div/div/div[2]").text
    #         print(" Create textCard success")
    #     except:
    #         print(" Create textCard failed !")
    #         #driver.get_log("driver")
    #     self.assertEqual("测试富文本卡", card_name, msg="创建富文本卡失败！")
    #
    # @BeautifulReport.add_test_img('test_f_TestCard')
    # def test_f_TestCard(self):
    #     '''创建测评卡'''
    #     testcard_name=""
    #     try:
    #         # 进入主页的备课系统按钮
    #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
    #         # 点击课程
    #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
    #         time.sleep(0.5)
    #         # 点击教学点模块按钮-new
    #         driver.find_element_by_xpath("//div[@class='Course']/div[3]/div/div[3]/div[2]/button").click()
    #         # 点击智能测评
    #         driver.find_element_by_link_text("智能测评").click()
    #         time.sleep(0.5)
    #         # 点击添加任务卡按钮
    #         driver.find_element_by_xpath("//div[@class='courseUnitSteps']/div[3]/div/div/div/div/div").click()
    #         time.sleep(1)
    #         # 点击添加测评卡按钮
    #         driver.find_element_by_xpath("//div[@class='ant-card lTaskCard lTaskCard-type-go ant-card-bordered']/div").click()
    #         time.sleep(1)
    #         # js = "var q=document.getElementByclassName('pMainCon').scrollTop=0"
    #         # driver.execute_script(js)
    #         #driver.execute_script("window.scrollBy(0,100)")
    #         # 点击选择形容词与副词
    #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[3]/div/div/div/div/div[1]/div[2]/div/div/div[6]/a/div/div[2]").click()
    #         # 点击创建按钮
    #         driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-lg']").click()
    #         time.sleep(1)
    #         testcard_name = driver.find_element_by_xpath("//div[@class='courseUnitSteps']/div[3]/div/div/div[1]/div/div/div/div/div[2]").text
    #         print("  Create testcard success!")
    #     except:
    #         print("Create testcard failed!")
    #         driver.get_log("driver")
    #     self.assertEqual("形容词与副词", testcard_name, msg="创建测评卡失败！")
    #
    # @BeautifulReport.add_test_img('test_g_Copyteachingpoint')
    # def test_g_Copyteachingpoint(self):
    #     '''拷贝教学点模块'''
    #     teachpointCopy_name=""
    #     try:
    #         # 进入主页的备课系统按钮
    #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
    #         # 点击课程
    #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
    #         time.sleep(1)
    #         # 滚动页面到底部
    #         #js = 'document.getElementsByClassName("Course")[0].scrollTop=10000'
    #         js = 'document.getElementsByClassName("Course")[0].scrollTop=1000'
    #         driver.execute_script(js)
    #         #driver.execute_script("window.scrollBy(0,100)")
    #         # 点击教学点模块按钮
    #         driver.find_element_by_xpath("//div[@class='ant-card-body']/div[2]/button").click()
    #         # 点击拷贝现有模块
    #         driver.find_element_by_link_text("拷贝现有模块").click()
    #         time.sleep(1)
    #         # 搜索要拷贝的课程
    #         driver.find_element_by_id("keyword").send_keys("富文本卡测试")
    #         # 点击搜索按钮
    #         driver.find_element_by_xpath("//button[@type='submit']").click()
    #         time.sleep(2)
    #         # 点击选择拷贝的课程-新方法
    #         driver.find_element_by_class_name("courseCard").click()
    #         time.sleep(1)
    #         # 点击拷贝教学点模块按钮
    #         driver.find_element_by_xpath("//div[@class='wCourseSelector isCourseDetail']/div/div[2]/div/div[3]/div/div[1]/div/h3/button").click()
    #         time.sleep(2)
    #         print(" Create copyteachingpoint success!")
    #         teachpointCopy_name = driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div[1]/div[4]/div/h3/div/div").text
    #     except:
    #         print("Create copyteachingpoint failed!")
    #         driver.log_types
    #         driver.get_log("driver")
    #     self.assertEqual("点的旋转_15.2 直角坐标平面内点的运动", teachpointCopy_name, msg="拷贝教学点模块失败！")
    #
    # @BeautifulReport.add_test_img('test_h_verifyMyCourseNotPass')
    # def test_h_verifyMyCourseNotPass(self):
    #     '''提交审核课程_不通过'''
    #     courseName= ""
    #     Rcourse_name=""
    #     review_state=""
    #     try:
    #         # 进入主页的备课系统按钮
    #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
    #         courseName = driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div/a/div[2]/div/div").text
    #         # 点击课程
    #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
    #         time.sleep(1)
    #         # 点击更多链接
    #         driver.find_element_by_link_text("更多").click()
    #         # 点击提交审核
    #         driver.find_element_by_xpath("//div[@class='ant-dropdown ant-dropdown-placement-bottomCenter']/ul/li[1]").click()
    #         # 点击输入框
    #         WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("marks"))
    #         driver.find_element_by_id("marks").click()
    #         # 输入审核课程说明内容
    #         driver.find_element_by_id("marks").send_keys("测试提交审核V1.0")
    #         time.sleep(0.5)
    #         # 点击确认按钮
    #         driver.find_element_by_xpath("//button[@type='submit']").click()
    #         time.sleep(0.5)
    #         # 点击课程审核
    #         driver.find_element_by_xpath("//*[@id='2$Menu']/li[4]").click()
    #         # 获取自动化课程名字
    #         Rcourse_name = driver.find_element_by_xpath("//div[@class='CourseCardList']/a[1]/div[2]/div[1]/div").text
    #         # 点击审核的课程
    #         driver.find_element_by_xpath("//div[@class='CourseCardList']/a[1]").click()
    #         # 点击不通过按钮
    #         driver.find_element_by_xpath("//div[@class='pPageHeaderTitle']/div/div/button[@class='ant-btn']").click()
    #         time.sleep(0.5)
    #         # 点击不通过理由输入框
    #         driver.find_element_by_xpath("//div[@class='ant-modal-body']/textarea").click()
    #         # 输入不通过理由
    #         driver.find_element_by_xpath("//div[@class='ant-modal-body']/textarea").send_keys("测试不通过")
    #         # 点击确定按钮
    #         driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-lg']").click()
    #         time.sleep(1)
    #         review_state = driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[2]/p[1]/span").text
    #         print("verifyMyCourseNotPass success!")
    #     except:
    #         print("verifyMyCourseNotPass failed!")
    #         driver.log_types
    #         driver.get_log("driver")
    #     self.assertEqual(courseName, Rcourse_name, msg="提交审核课程失败！")
    #     self.assertEqual("审核状态： 不通过", review_state, msg="审核不通过失败")
    #
    #
    # @BeautifulReport.add_test_img('test_i_verifyMyCoursePass')
    # def test_i_verifyMyCoursePass(self):
    #     '''提交审核课程_通过，我的课程到学校课程'''
    #     courseName = ""
    #     Rcourse_name = ""
    #     review_state = ""
    #     schoolCourse= ""
    #     try:
    #         # 进入主页的备课系统按钮
    #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
    #         courseName = driver.find_element_by_xpath(
    #             "//div[@class='wCardsLayout']/div/div[1]/div/div/a/div[2]/div/div").text
    #         # 点击课程
    #         driver.find_element_by_xpath(
    #             "//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
    #         time.sleep(1)
    #         # 点击更多链接
    #         driver.find_element_by_link_text("更多").click()
    #         # 点击提交审核
    #         driver.find_element_by_xpath("//div[@class='ant-dropdown ant-dropdown-placement-bottomCenter']/ul/li[1]").click()
    #         # 点击输入框
    #         WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("marks"))
    #         driver.find_element_by_id("marks").click()
    #         # 输入审核课程说明内容
    #         driver.find_element_by_id("marks").send_keys("测试提交审核V2.0")
    #         time.sleep(1)
    #         # 点击确认按钮
    #         driver.find_element_by_xpath("//button[@type='submit']").click()
    #         time.sleep(1)
    #         # 点击课程审核
    #         driver.find_element_by_xpath("//*[@id='2$Menu']/li[4]").click()
    #         # 获取自动化课程名字
    #         Rcourse_name = driver.find_element_by_xpath("//div[@class='CourseCardList']/a[1]/div[2]/div[1]/div").text
    #         # 点击审核的课程
    #         driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div/a").click()
    #         # 点击通过按钮
    #         driver.find_element_by_xpath("//div[@class='pPageHeaderTitle']/div/div/button[1]").click()
    #         time.sleep(0.5)
    #         # 点击确定按钮
    #         driver.find_element_by_xpath("//div[@class='ant-confirm-btns']/button[2]").click()
    #         time.sleep(0.5)
    #         review_state = driver.find_element_by_xpath("//div[@class='stateContent suss']/p[1]/span").text
    #         # 点击学校课程
    #         driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline  ant-menu-sub']/li[2]/div").click()
    #         time.sleep(0.5)
    #         schoolCourse = driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div/a/div[2]/div[1]/div").text
    #         print("verifyMyCoursePass success!")
    #     except:
    #         print("verifyMyCoursePass failed!")
    #         driver.log_types
    #         driver.get_log("driver")
    #     self.assertEqual(courseName, Rcourse_name, msg="提交审核课程失败！")
    #     self.assertEqual("审核状态： 通过", review_state, msg="审核通过失败")
    #     self.assertEqual(courseName, schoolCourse, msg="学校课程不存在审核通过的课程")
    #
    # @BeautifulReport.add_test_img('test_j_schoolCourseToMarketcourse')
    # def test_j_schoolCourseToMarketcourse(self):
    #     '''学校课程发布到课程市场'''
    #     courseName = ""
    #     release_state = ""
    #     marketCourse = ""
    #     try:
    #         # 进入主页的备课系统按钮
    #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
    #         # 点击学校课程
    #         driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline  ant-menu-sub']/li[2]").click()
    #         # 获取学校课程第一门课的课程名字
    #         courseName = driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div/a/div[2]/div/div").text
    #         # 输入要发布的课程名字
    #         driver.find_element_by_id("keyword").send_keys(courseName)
    #         # 搜索要发布的课程
    #         driver.find_element_by_xpath("//form/div[6]/div/div/button").click()
    #         # 点击第一门课进入
    #         driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]").click()
    #         #点击发布课程按钮
    #         driver.find_element_by_xpath("//div[@class='pPageHeaderTitle']/div/div/button").click()
    #         time.sleep(0.5)
    #         # 点击确定按钮
    #         driver.find_element_by_xpath("//div[@class='ant-confirm-btns']/button[2]").click()
    #         time.sleep(1)
    #         # 获取发布状态
    #         release_state = driver.find_element_by_xpath("//div[@class='pPageHeaderTitle']/div/div/span/button/span").text
    #         time.sleep(0.5)
    #         # 点击课程市场
    #         driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline  ant-menu-sub']/li[3]").click()
    #         time.sleep(1)
    #         marketCourse = driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div[1]/a/div[2]/div[1]/div").text
    #         print("schoolCourseToMarketcourse success!")
    #     except:
    #         print("schoolCourseToMarketcourse failed!")
    #         driver.log_types
    #         driver.get_log("driver")
    #     self.assertEqual("已发布", release_state, msg="确认后显示已发布")
    #     self.assertEqual(marketCourse, courseName, msg="成功发布到课程市场")


#if __name__ == '__main__':
#unittest.main()

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

testsuite = unittest.TestSuite()
# testsuite.addTest(Teacher4TestCase("test__1_creatCourse"))
# testsuite.addTest(Teacher4TestCase("test_IntelligenceCard"))
# testsuite.addTest(Teacher4TestCase("test_textcard"))
# testsuite.addTest(Teacher4TestCase("test_TestCrad"))
# testsuite.addTest(Teacher4TestCase("test_teachpointCopy"))
# testsuite.addTest(Teacher4TestCase("test_reviewMyCourse"))


testsuite.addTests(unittest.makeSuite(Teacher4TestCase))

run = BeautifulReport(testsuite)
#run.report(filename='教师端测试报告2'+now+'.html', description='备课系统测试', log_path='.')
#run.report(filename='教师端测试报告2'+now+'.html', description='备课系统测试', report_dir='report')
# mac 路径import os
# from common.commonConfig import CommonConfig
# import time
# import unittest
# import ApiTest
# import conMysql
# from selenium import webdriver
# #from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# from selenium.webdriver.common.by import By
#
# from BeautifulReport import BeautifulReport
#
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Teacher4TestCase(unittest.TestCase):
#
#
#     def setUp(self):
#         try:
#             global driver
#             # mac
#             path = CommonConfig.getPath(self)
#             # linux路径
#             #path = "/usr/local/python3/chromedriver"
#             url = CommonConfig.getUrl("TypeUrl", "teacherxUrl")
#
#             # linux使用的静默执行方法
#             # options = webdriver.ChromeOptions()
#             # options.add_argument('--headless')
#             # options.add_argument('--disable-gpu')
#             # options.add_argument('--no-sandbox')
#
#             # 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
#             #options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/Default')
#             # linux配置
#             # driver = webdriver.Chrome(executable_path=path, chrome_options=options)
#             driver = webdriver.Chrome(executable_path=path)
#             driver.implicitly_wait(20)
#             driver.get(url)
#             driver.maximize_window()
#             print(u"\nLogin start!")
#             driver.find_element_by_xpath("//span[@class='ant-select-arrow']").click()
#             driver.find_element_by_xpath("//ul[@class='ant-select-dropdown-menu ant-select-dropdown-menu-vertical  ant-select-dropdown-menu-root']/li[1]").click()
#             driver.find_element_by_id("username").send_keys("18817572035")
#             driver.find_element_by_id("code").send_keys("1111")
#             #点击登录按钮
#             driver.find_element_by_xpath("//button[@type='submit']").click()
#             #Log.info("setp_login ending...")
#             print("Login Success!")
#         except :
#             print("登录失败")
#
#     def tearDown(self):
#         try:
#             driver.close()
#         except:
#             print("close fail")
#
#
#     def click(self, loc):
#         try:
#             wait = WebDriverWait(driver, 10)
#             wait.until(EC.presence_of_element_located(By.XPATH, loc))
#             return True
#         except:
#             print(u'元素点击失败！')
#             #self.saveScreenShot_error('元素点击失败')
#             return False
#
#     def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
#         """
#             传入一个img_name, 并存储到默认的文件路径下
#         :param img_name:
#         :return:
#         """
#         # mac存放图片路径
#         driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"/Users/shuping/Python_code/SeleniumTest/img"), img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径
#         # mac存放图片路径2
#         #driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"/Users/shuping/.jenkins/workspace/autotest/img"), img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径
#         # linux存放图片路径
#         #driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"/usr/local/python3/img"), img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径
#
#     # 判断元素是否存在的方法
#     def isElementExist(self, element):
#         flag = True
#         try:
#             # locator2 = (By.XPATH, element)
#             # WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator2))
#             driver.implicitly_wait(5)
#             if driver.find_element_by_xpath(element):
#                 return flag
#         except:
#             flag = False
#             return flag
#
#     def isElementExistclass(self, element):
#         flag = True
#         try:
#             if driver.find_element_by_class_name(element):
#                 return flag
#         except:
#             flag = False
#             return flag
#
#     @BeautifulReport.add_test_img('test_1_right')
#     def test_1_right(self):
#         '''招生测评英语五年级——做对'''
#         testperson=""
#         try:
#             #  登录后点击招生测评模块
#             driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div/div[2]/div[6]").click()
#             # 点击立即分享
#             driver.find_element_by_xpath(
#                 "//*[@id='root']/div/div/main/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/span[1]").click()
#             # window_1 = driver.window_handles
#             # window_2 = driver.current_window_handle
#             time.sleep(1)
#             # turl = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[3]/div[2]/a/span").text
#             turl = driver.find_element_by_xpath("//div[@class='img-url']/a/span").text
#             newwindow = "window.open(\"" + turl + "\");"
#             # js = 'window.open("https://shupingorg.t1.learnta.cn/teacher4");'
#             driver.execute_script(newwindow)
#             window1 = driver.window_handles
#             # 跳转到新标签页
#             driver.switch_to.window(window1[1])
#             time.sleep(1)
#             # 输入姓名
#             # driver.find_element_by_name("username").send_keys("测试招生测评_复制链接")
#             driver.find_element_by_xpath("//form[@class='cSign__form']/div[1]/input").send_keys("测试招生测评_复制链接")
#             # 输入手机号
#             driver.find_element_by_xpath("//form[@class='cSign__form']/div[2]/input").send_keys("18817572035")
#             # driver.find_element_by_name("mobile").send_keys("18817572035")
#             # 输入验证码
#             driver.find_element_by_xpath("//form[@class='cSign__form']/div[3]/input").send_keys("1111")
#             # driver.find_element_by_name("code").send_keys("1111")
#             # 点击选择地区下拉框
#             driver.find_element_by_xpath("//span[@class='ant-cascader-picker']").click()
#             # driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[4]/span/input").click()
#             # 点击选择天津（省）
#             driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[1]/li[2]").click()
#             # driver.find_element_by_xpath("/body/div[3]/div/div/div/ul[1]/li[2]").click()
#             # 选择天津市
#             driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[2]/li[1]").click()
#             # 选择和平区
#             driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[3]/li[1]").click()
#             # 再点击一次筛选地区筛选框
#             driver.find_element_by_xpath("//div[@class='recTitle']").click()
#             # js = "var q=document.getElementByclassName('pMainCon').scrollTop=0"
#             # driver.execute_script(js)
#             # 滚动页面的滚动条
#             driver.execute_script("window.scrollBy(0,100)")
#             # 点击登录，开始测评
#             driver.find_element_by_xpath("//form[@class='cSign__form']/a/span").click()
#             time.sleep(0.5)
#             name = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/ul/li[1]").text
#             # 点击开始测评
#             driver.find_element_by_xpath("//div[@class='step step-1']/ul/li[1]").click()
#             # 选择英语
#             driver.find_element_by_xpath("//div[@class='step step-1']/ul/li[1]").click()
#             # driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/ul/li[1]").click()
#             # 点击五年级
#             driver.find_element_by_xpath("//div[@class='step step-2']/ul/li[2]").click()
#             # 循环点击专题下一题按钮
#             elementflag = self.isElementExist("//div[@class='btnWrapper']/a[2]")
#             # elementflag = self.isElementExist("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]")
#             while (elementflag):
#                 time.sleep(0.5)
#                 proquestionId = ApiTest.ApiTest.test_get_01(self)
#                 qlist = ApiTest.ApiTest.test_post_01(self, proquestionId)
#                 # 如果是选择题
#                 if qlist[1] == 0:
#                     # 查询题目的答案
#                     answer_2 = conMysql.ConnMysql.testOption(self, qlist[0])
#                     if answer_2 == "A":
#                         driver.find_element_by_xpath(
#                             "//*[@id='root']/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li[1]").click()
#                         # 点击下一题按钮
#                         driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
#                     elif answer_2 == "B":
#                         driver.find_element_by_xpath(
#                             "//*[@id='root']/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li[2]").click()
#                         # 点击下一题按钮
#                         driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
#                     elif answer_2 == "C":
#                         driver.find_element_by_xpath(
#                             "//*[@id='root']/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li[3]").click()
#                         # 点击下一题按钮
#                         driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
#                     elif answer_2 == "D":
#                         driver.find_element_by_xpath(
#                             "//*[@id='root']/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/ul/li[4]").click()
#                         # 点击下一题按钮
#                         driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
#                 elif qlist[1] == 1:  # 如果是填空题
#                     answerblank = conMysql.ConnMysql.test_blank(self, qlist[0])
#                     inputlist = driver.find_elements_by_xpath("//input[@class='gapInput']")
#                     for i in range(len(inputlist)):
#                         inputlist[i].send_keys(answerblank[i])
#                     # 点击下一题按钮
#                     driver.find_element_by_xpath(".//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]").click()
#                     # 点击弹窗的确定按钮
#                 elementflag = self.isElementExist("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]")
#
#             reportname = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div[2]/p[2]").text
#             print("测评报告：", reportname)
#             testperson = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div[1]/p").text
#             print("测试人：", testperson)
#
#             score = driver.find_element_by_xpath("//*[@id='analyzeReport']/div/div[1]/div[1]/p[2]").text
#             print("得分：", score)
#         except:
#             print("test allright fail!")
#         self.assertEqual("ceshi", testperson)
#
#     @BeautifulReport.add_test_img('test_2_wrong')
#     def test_2_wrong(self):
#         '''招生测评英语五年级——全做错'''
#         testperson=""
#         try:
#             # 登录后点击招生测评模块
#             # driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[3]/div[3]/div[2]").click()
#             driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div/div[2]/div[6]").click()
#
#             # 点击登录后的招生测评
#             # driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[3]/div[2]").click()
#             time.sleep(1)
#             # 点击立即分享
#             driver.find_element_by_xpath(
#                 "//*[@id='root']/div/div/main/div/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/span[1]").click()
#             time.sleep(1)
#             # window_1 = driver.window_handles
#             # window_2 = driver.current_window_handle
#             turl = driver.find_element_by_xpath("//div[@class='img-url']/a/span").text
#             newwindow = "window.open(\"" + turl + "\");"
#             driver.execute_script(newwindow)
#             window1 = driver.window_handles
#             # 跳转到新标签页
#             driver.switch_to.window(window1[1])
#             time.sleep(1)
#             # 输入姓名
#             driver.find_element_by_name("username").send_keys("测试招生测评_复制链接")
#             # 输入手机号
#             driver.find_element_by_name("mobile").send_keys("18817572035")
#             # 输入验证码
#             driver.find_element_by_name("code").send_keys("1111")
#             # 点击选择地区下拉框
#             driver.find_element_by_xpath("//span[@class='ant-cascader-picker']").click()
#             # 点击选择天津（省）
#             driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[1]/li[2]").click()
#             # 选择天津市
#             driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[2]/li[1]").click()
#             # 选择和平区
#             driver.find_element_by_xpath("//body/div[4]/div/div/div/ul[3]/li[1]").click()
#             # 再点击一次筛选地区筛选框
#             driver.find_element_by_xpath("//div[@class='recTitle']").click()
#             # 滚动页面的滚动条
#             driver.execute_script("window.scrollBy(0,100)")
#             # 点击登录，开始测评
#             driver.find_element_by_xpath("//form/a/span").click()
#             time.sleep(1)
#             name = driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div/ul/li[1]").text
#             # 点击开始测评
#             driver.find_element_by_xpath("//div[@class='step step-1']/ul/li[1]").click()
#             # 选择英语
#             driver.find_element_by_xpath("//div[@class='step step-1']/ul/li[1]").click()
#             # 点击五年级
#             driver.find_element_by_xpath("//div[@class='step step-2']/ul/li[2]").click()
#
#             # 循环点击专题下一题按钮
#             elementflag = self.isElementExist("//div[@class='btnWrapper']/a[2]")
#             while (elementflag):
#                 driver.find_element_by_xpath("//div[@class='btnWrapper']/a[2]").click()
#                 time.sleep(0.5)
#                 # 点击弹窗的确定按钮
#                 driver.find_element_by_xpath("//div[@class='ant-confirm-btns']/button[2]").click()
#                 time.sleep(0.5)
#                 # 下一题按钮是否存在
#                 elementflag = self.isElementExist("//div[@class='btnWrapper']/a[2]")
#
#             reportname = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div[2]/p[2]").text
#             print("测评报告：", reportname)
#             testperson = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div[2]/div[1]/p").text
#             print("测试人：", testperson)
#             score = driver.find_element_by_xpath("//*[@id='analyzeReport']/div/div[1]/div[1]/p[2]").text
#             print("得分：", score)
#             # self.assertEqual("测评报告", reportname)
#         except:
#             print("test wrong fail")
#         self.assertEqual("ceshi", testperson)
#         driver.close()
#         driver.quit()
#
#     # @BeautifulReport.add_test_img('test_c_creatCourse')
#     # def test_c_creatCourse(self):
#     #     '''创建课程'''
#     #     now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
#     #     courseName = ""
#     #     ResultcourseName = ""
#     #     try:
#     #         print("Create course start !")
#     #         time.sleep(1)
#     #         #进入主页的备课系统按钮
#     #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
#     #         time.sleep(1)
#     #         # 点击创建课程按钮
#     #         driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-lg pullRight createBtn noCopyBtn']").click()
#     #         time.sleep(1)
#     #         #点击选择数学
#     #         driver.find_element_by_xpath("//form/div[1]/div[2]/div/div/label[2]").click()
#     #         #点击选择沪教版
#     #         driver.find_element_by_xpath("//form/div[2]/div[2]/div/div/label[5]").click()
#     #         time.sleep(1)
#     #         #点击输入课程名称
#     #         courseName = "自动化测试课程" + now
#     #         driver.find_element_by_xpath("//*[@id='courseName']").send_keys(courseName)
#     #         # 点击确定按钮
#     #         driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
#     #         # 点击选择年级下拉框按钮
#     #         driver.find_element_by_xpath("//div[@class='wrapper selectWrapper wrapper-default']/span").click()
#     #         # 点击五年级
#     #         driver.find_element_by_xpath("//div[@class='ant-cascader-menus ant-cascader-menus-placement-bottomLeft']/div/ul[1]/li[5]").click()
#     #         # 点击选择五年级上
#     #         driver.find_element_by_xpath("//div[@class='ant-cascader-menus ant-cascader-menus-placement-bottomLeft']/div/ul[2]/li[1]").click()
#     #         time.sleep(1)
#     #         # 点击添加单元按钮
#     #         driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-ghost ant-btn-lg addButton']").click()
#     #         time.sleep(1)
#     #         # 点击选择新的单元
#     #         driver.find_element_by_xpath("//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical  ant-dropdown-menu-light ant-dropdown-menu-root']/li[2]").click()
#     #         print("  Add unit success ...")
#     #         # 点击添加教学点模块下拉框
#     #         driver.find_element_by_xpath("//div[@class='Course']/div[3]/div/div[3]/div[2]/button").click()
#     #         time.sleep(1)
#     #         # 点击选择教学点模块
#     #         driver.find_element_by_link_text("教学点模块").click()
#     #         time.sleep(1)
#     #         print("  Add jiaoxuedian success ...")
#     #         #点击选择教学点下拉框
#     #         driver.find_element_by_xpath("//div[@class='ant-modal-body']/span").click()
#     #         # 点击八年级上册下拉按钮
#     #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/span").click()
#     #         #点击第十一章三角形下拉按钮
#     #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/ul/li[1]/span").click()
#     #         # 点击11.1按钮
#     #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/ul/li[1]/ul/li[1]/span").click()
#     #         # 点选择 11.1.1
#     #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/ul/li[1]/ul/li[1]/ul/li[1]/span").click()
#     #         time.sleep(1)
#     #         # 点击选择三角形的三边关系（可选）
#     #         driver.find_element_by_xpath("//ul[@class='ant-select-tree']/li[1]/ul/li[1]/ul/li[1]/ul/li[1]/ul/li/a/span").click()
#     #         time.sleep(1)
#     #         # 点击确定按钮
#     #         driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
#     #         # 创建完课程取课程名字
#     #         ResultcourseName = driver.find_element_by_class_name("headerTitle").text
#     #         print("Create course success! ")
#     #     except:
#     #         print("Create course failed!")
#     #     self.assertEqual(courseName, ResultcourseName, msg="创建课程失败!")
#     #
#     # @BeautifulReport.add_test_img('test_d_IntelligenceCard')
#     # def test_d_IntelligenceCard(self):
#     #     '''创建智能练习卡 '''
#     #     #driver = driver
#     # #   kk = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("kw"), message="worry!")
#     #     cardName=""
#     #     try:
#     #         # 进入主页的备课系统按钮
#     #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
#     #         # 点击课程
#     #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
#     #         #time.sleep(1)
#     #         # 设置等待添加按钮时间后点击按钮
#     #         # locator2 = (By.XPATH, "//button[@class='ant-card lTaskCard lTaskCard-type-add ant-card-bordered']")
#     #         # WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator2))
#     #         # 点击添加按钮
#     #         driver.find_element_by_xpath("//div[@class='lCourseUnitStep']/div/div[last()]/div").click()
#     #         time.sleep(1)
#     #         # 点击添加智能练习卡按钮
#     #         driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[5]/a").click()
#     #         time.sleep(1)
#     #         # 点击创建按钮
#     #         driver.find_element_by_xpath("//button[@type='submit']").click()
#     #         #time.sleep(1)
#     #         print("  Add intelligenceCard success ...")
#     #         # 创建完课程取课程名字
#     #         #courseName = driver.find_element_by_class_name("headerTitle").text
#     #         cardName = driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div[1]/div/div/div/div[5]/div/div/div/div/div[2]").text
#     #         print("Create intelligenceCard success!")
#     #     except:
#     #         print("Create intelligenceCard error!")
#     #     self.assertEqual("二次根式的概念", cardName, msg="创建智能练习卡失败！")
#     #
#     # @BeautifulReport.add_test_img('test_e_textcard')
#     # def test_e_textcard(self):
#     #     '''创建富文本卡'''
#     #     card_name=""
#     #     try:
#     #         # page = driver.page_source  #获取源码
#     #         # doc = pq(page)
#     #         # doc = etree.HTML(str(doc))
#     #         # contents = doc.xpath('//div[@class="ant-card-body"]/div[1]/div/div/div')
#     #         #
#     #         # for x in contents:
#     #         #     x.xpath("/div[5]/div")
#     #         # 进入主页的备课系统按钮
#     #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
#     #         # 点击课程
#     #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
#     #         # 点击教学点模块
#     #         driver.find_element_by_xpath("//div[@class='ant-card-body']/div[2]/button").click()
#     #         #driver.find_element_by_link_text("教学点模块").click()
#     #         # 点击教学活动
#     #         driver.find_element_by_link_text("教学活动").click()
#     #         #driver.find_element_by_xpath("/html/body/div[4]/div/div/ul/li[2]").click()
#     #         time.sleep(1)
#     #         # 点击添加任务卡按钮
#     #         driver.find_element_by_xpath("//div[@class='courseUnitSteps']/div[2]/div/div/div/div/div").click()
#     #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div[1]/div[2]/div/div/div/div").click()
#     #         time.sleep(1)
#     #         # 点击选择富文本卡按钮
#     #         driver.find_element_by_xpath("//div[@class='ant-card lTaskCard lTaskCard-type-rich_text ant-card-bordered']/div").click()
#     #         #driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/div/div/a/div").click()
#     #
#     #         driver.find_element_by_id("taskName").send_keys("测试富文本卡")
#     #         time.sleep(0.5)
#     #         # 点击react-box获取焦点
#     #         driver.find_element_by_xpath("//div[@class='ant-row ant-form-item introductionFormItem']/div[2]/div/div/div/div[2]").click()
#     #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[3]/div[2]/div/div/div").click()
#     #         # 输入备注文本
#     #         driver.find_element_by_xpath("//div[@class='ant-row ant-form-item introductionFormItem']/div[2]/div/div/div/div[2]").send_keys("测试添加备注内容")
#     #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[3]/div[2]/div/div/div/div[2]").send_keys("测试添加备注内容")
#     #         time.sleep(0.5)
#     #         # 获取任务描述的焦点
#     #         driver.find_element_by_xpath("//div[@class='ant-row ant-form-item taskDataFormItem']/div[2]/div/div/div[1]/div/div[2]").click()
#     #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[4]/div[2]/div/div/div").click()
#     #         # 输入任务描述的文本
#     #         driver.find_element_by_xpath("//div[@class='ant-row ant-form-item taskDataFormItem']/div[2]/div/div/div[1]/div/div[2]").send_keys("测试添加富文本卡任务描述内容")
#     #         #driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[4]/div[2]/div/div/div/div[2]").send_keys("测试添加富文本卡任务描述内容")
#     #         time.sleep(0.5)
#     #         # 点击创建按钮
#     #         driver.find_element_by_xpath("//button[@class ='ant-btn ant-btn-primary ant-btn-lg']").click()
#     #         card_name=driver.find_element_by_xpath("//div[@class='courseUnitSteps']/div[2]/div/div/div[1]/div//div/div/div/div[2]").text
#     #         print(" Create textCard success")
#     #     except:
#     #         print(" Create textCard failed !")
#     #         #driver.get_log("driver")
#     #     self.assertEqual("测试富文本卡", card_name, msg="创建富文本卡失败！")
#     #
#     # @BeautifulReport.add_test_img('test_f_TestCard')
#     # def test_f_TestCard(self):
#     #     '''创建测评卡'''
#     #     testcard_name=""
#     #     try:
#     #         # 进入主页的备课系统按钮
#     #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
#     #         # 点击课程
#     #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
#     #         time.sleep(0.5)
#     #         # 点击教学点模块按钮-new
#     #         driver.find_element_by_xpath("//div[@class='Course']/div[3]/div/div[3]/div[2]/button").click()
#     #         # 点击智能测评
#     #         driver.find_element_by_link_text("智能测评").click()
#     #         time.sleep(0.5)
#     #         # 点击添加任务卡按钮
#     #         driver.find_element_by_xpath("//div[@class='courseUnitSteps']/div[3]/div/div/div/div/div").click()
#     #         time.sleep(1)
#     #         # 点击添加测评卡按钮
#     #         driver.find_element_by_xpath("//div[@class='ant-card lTaskCard lTaskCard-type-go ant-card-bordered']/div").click()
#     #         time.sleep(1)
#     #         # js = "var q=document.getElementByclassName('pMainCon').scrollTop=0"
#     #         # driver.execute_script(js)
#     #         #driver.execute_script("window.scrollBy(0,100)")
#     #         # 点击选择形容词与副词
#     #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div[2]/form/div[3]/div/div/div/div/div[1]/div[2]/div/div/div[6]/a/div/div[2]").click()
#     #         # 点击创建按钮
#     #         driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-lg']").click()
#     #         time.sleep(1)
#     #         testcard_name = driver.find_element_by_xpath("//div[@class='courseUnitSteps']/div[3]/div/div/div[1]/div/div/div/div/div[2]").text
#     #         print("  Create testcard success!")
#     #     except:
#     #         print("Create testcard failed!")
#     #         driver.get_log("driver")
#     #     self.assertEqual("形容词与副词", testcard_name, msg="创建测评卡失败！")
#     #
#     # @BeautifulReport.add_test_img('test_g_Copyteachingpoint')
#     # def test_g_Copyteachingpoint(self):
#     #     '''拷贝教学点模块'''
#     #     teachpointCopy_name=""
#     #     try:
#     #         # 进入主页的备课系统按钮
#     #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
#     #         # 点击课程
#     #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
#     #         time.sleep(1)
#     #         # 滚动页面到底部
#     #         #js = 'document.getElementsByClassName("Course")[0].scrollTop=10000'
#     #         js = 'document.getElementsByClassName("Course")[0].scrollTop=1000'
#     #         driver.execute_script(js)
#     #         #driver.execute_script("window.scrollBy(0,100)")
#     #         # 点击教学点模块按钮
#     #         driver.find_element_by_xpath("//div[@class='ant-card-body']/div[2]/button").click()
#     #         # 点击拷贝现有模块
#     #         driver.find_element_by_link_text("拷贝现有模块").click()
#     #         time.sleep(1)
#     #         # 搜索要拷贝的课程
#     #         driver.find_element_by_id("keyword").send_keys("富文本卡测试")
#     #         # 点击搜索按钮
#     #         driver.find_element_by_xpath("//button[@type='submit']").click()
#     #         time.sleep(2)
#     #         # 点击选择拷贝的课程-新方法
#     #         driver.find_element_by_class_name("courseCard").click()
#     #         time.sleep(1)
#     #         # 点击拷贝教学点模块按钮
#     #         driver.find_element_by_xpath("//div[@class='wCourseSelector isCourseDetail']/div/div[2]/div/div[3]/div/div[1]/div/h3/button").click()
#     #         time.sleep(2)
#     #         print(" Create copyteachingpoint success!")
#     #         teachpointCopy_name = driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div[1]/div[4]/div/h3/div/div").text
#     #     except:
#     #         print("Create copyteachingpoint failed!")
#     #         driver.log_types
#     #         driver.get_log("driver")
#     #     self.assertEqual("点的旋转_15.2 直角坐标平面内点的运动", teachpointCopy_name, msg="拷贝教学点模块失败！")
#     #
#     # @BeautifulReport.add_test_img('test_h_verifyMyCourseNotPass')
#     # def test_h_verifyMyCourseNotPass(self):
#     #     '''提交审核课程_不通过'''
#     #     courseName= ""
#     #     Rcourse_name=""
#     #     review_state=""
#     #     try:
#     #         # 进入主页的备课系统按钮
#     #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
#     #         courseName = driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div/a/div[2]/div/div").text
#     #         # 点击课程
#     #         driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
#     #         time.sleep(1)
#     #         # 点击更多链接
#     #         driver.find_element_by_link_text("更多").click()
#     #         # 点击提交审核
#     #         driver.find_element_by_xpath("//div[@class='ant-dropdown ant-dropdown-placement-bottomCenter']/ul/li[1]").click()
#     #         # 点击输入框
#     #         WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("marks"))
#     #         driver.find_element_by_id("marks").click()
#     #         # 输入审核课程说明内容
#     #         driver.find_element_by_id("marks").send_keys("测试提交审核V1.0")
#     #         time.sleep(0.5)
#     #         # 点击确认按钮
#     #         driver.find_element_by_xpath("//button[@type='submit']").click()
#     #         time.sleep(0.5)
#     #         # 点击课程审核
#     #         driver.find_element_by_xpath("//*[@id='2$Menu']/li[4]").click()
#     #         # 获取自动化课程名字
#     #         Rcourse_name = driver.find_element_by_xpath("//div[@class='CourseCardList']/a[1]/div[2]/div[1]/div").text
#     #         # 点击审核的课程
#     #         driver.find_element_by_xpath("//div[@class='CourseCardList']/a[1]").click()
#     #         # 点击不通过按钮
#     #         driver.find_element_by_xpath("//div[@class='pPageHeaderTitle']/div/div/button[@class='ant-btn']").click()
#     #         time.sleep(0.5)
#     #         # 点击不通过理由输入框
#     #         driver.find_element_by_xpath("//div[@class='ant-modal-body']/textarea").click()
#     #         # 输入不通过理由
#     #         driver.find_element_by_xpath("//div[@class='ant-modal-body']/textarea").send_keys("测试不通过")
#     #         # 点击确定按钮
#     #         driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-lg']").click()
#     #         time.sleep(1)
#     #         review_state = driver.find_element_by_xpath("//*[@id='root']/div/div/main/div/div[1]/div/div/div[2]/p[1]/span").text
#     #         print("verifyMyCourseNotPass success!")
#     #     except:
#     #         print("verifyMyCourseNotPass failed!")
#     #         driver.log_types
#     #         driver.get_log("driver")
#     #     self.assertEqual(courseName, Rcourse_name, msg="提交审核课程失败！")
#     #     self.assertEqual("审核状态： 不通过", review_state, msg="审核不通过失败")
#     #
#     #
#     # @BeautifulReport.add_test_img('test_i_verifyMyCoursePass')
#     # def test_i_verifyMyCoursePass(self):
#     #     '''提交审核课程_通过，我的课程到学校课程'''
#     #     courseName = ""
#     #     Rcourse_name = ""
#     #     review_state = ""
#     #     schoolCourse= ""
#     #     try:
#     #         # 进入主页的备课系统按钮
#     #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
#     #         courseName = driver.find_element_by_xpath(
#     #             "//div[@class='wCardsLayout']/div/div[1]/div/div/a/div[2]/div/div").text
#     #         # 点击课程
#     #         driver.find_element_by_xpath(
#     #             "//*[@id='root']/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div[1]/div/div/a/div[2]/div[1]/div").click()
#     #         time.sleep(1)
#     #         # 点击更多链接
#     #         driver.find_element_by_link_text("更多").click()
#     #         # 点击提交审核
#     #         driver.find_element_by_xpath("//div[@class='ant-dropdown ant-dropdown-placement-bottomCenter']/ul/li[1]").click()
#     #         # 点击输入框
#     #         WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id("marks"))
#     #         driver.find_element_by_id("marks").click()
#     #         # 输入审核课程说明内容
#     #         driver.find_element_by_id("marks").send_keys("测试提交审核V2.0")
#     #         time.sleep(1)
#     #         # 点击确认按钮
#     #         driver.find_element_by_xpath("//button[@type='submit']").click()
#     #         time.sleep(1)
#     #         # 点击课程审核
#     #         driver.find_element_by_xpath("//*[@id='2$Menu']/li[4]").click()
#     #         # 获取自动化课程名字
#     #         Rcourse_name = driver.find_element_by_xpath("//div[@class='CourseCardList']/a[1]/div[2]/div[1]/div").text
#     #         # 点击审核的课程
#     #         driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div/a").click()
#     #         # 点击通过按钮
#     #         driver.find_element_by_xpath("//div[@class='pPageHeaderTitle']/div/div/button[1]").click()
#     #         time.sleep(0.5)
#     #         # 点击确定按钮
#     #         driver.find_element_by_xpath("//div[@class='ant-confirm-btns']/button[2]").click()
#     #         time.sleep(0.5)
#     #         review_state = driver.find_element_by_xpath("//div[@class='stateContent suss']/p[1]/span").text
#     #         # 点击学校课程
#     #         driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline  ant-menu-sub']/li[2]/div").click()
#     #         time.sleep(0.5)
#     #         schoolCourse = driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div/a/div[2]/div[1]/div").text
#     #         print("verifyMyCoursePass success!")
#     #     except:
#     #         print("verifyMyCoursePass failed!")
#     #         driver.log_types
#     #         driver.get_log("driver")
#     #     self.assertEqual(courseName, Rcourse_name, msg="提交审核课程失败！")
#     #     self.assertEqual("审核状态： 通过", review_state, msg="审核通过失败")
#     #     self.assertEqual(courseName, schoolCourse, msg="学校课程不存在审核通过的课程")
#     #
#     # @BeautifulReport.add_test_img('test_j_schoolCourseToMarketcourse')
#     # def test_j_schoolCourseToMarketcourse(self):
#     #     '''学校课程发布到课程市场'''
#     #     courseName = ""
#     #     release_state = ""
#     #     marketCourse = ""
#     #     try:
#     #         # 进入主页的备课系统按钮
#     #         driver.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div[2]/div[2]/div[2]").click()
#     #         # 点击学校课程
#     #         driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline  ant-menu-sub']/li[2]").click()
#     #         # 获取学校课程第一门课的课程名字
#     #         courseName = driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div/a/div[2]/div/div").text
#     #         # 输入要发布的课程名字
#     #         driver.find_element_by_id("keyword").send_keys(courseName)
#     #         # 搜索要发布的课程
#     #         driver.find_element_by_xpath("//form/div[6]/div/div/button").click()
#     #         # 点击第一门课进入
#     #         driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]").click()
#     #         #点击发布课程按钮
#     #         driver.find_element_by_xpath("//div[@class='pPageHeaderTitle']/div/div/button").click()
#     #         time.sleep(0.5)
#     #         # 点击确定按钮
#     #         driver.find_element_by_xpath("//div[@class='ant-confirm-btns']/button[2]").click()
#     #         time.sleep(1)
#     #         # 获取发布状态
#     #         release_state = driver.find_element_by_xpath("//div[@class='pPageHeaderTitle']/div/div/span/button/span").text
#     #         time.sleep(0.5)
#     #         # 点击课程市场
#     #         driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline  ant-menu-sub']/li[3]").click()
#     #         time.sleep(1)
#     #         marketCourse = driver.find_element_by_xpath("//div[@class='wCardsLayout']/div/div[1]/div/div[1]/a/div[2]/div[1]/div").text
#     #         print("schoolCourseToMarketcourse success!")
#     #     except:
#     #         print("schoolCourseToMarketcourse failed!")
#     #         driver.log_types
#     #         driver.get_log("driver")
#     #     self.assertEqual("已发布", release_state, msg="确认后显示已发布")
#     #     self.assertEqual(marketCourse, courseName, msg="成功发布到课程市场")
#
#
# #if __name__ == '__main__':
# #unittest.main()
#
# now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
#
# testsuite = unittest.TestSuite()
# # testsuite.addTest(Teacher4TestCase("test__1_creatCourse"))
# # testsuite.addTest(Teacher4TestCase("test_IntelligenceCard"))
# # testsuite.addTest(Teacher4TestCase("test_textcard"))
# # testsuite.addTest(Teacher4TestCase("test_TestCrad"))
# # testsuite.addTest(Teacher4TestCase("test_teachpointCopy"))
# # testsuite.addTest(Teacher4TestCase("test_reviewMyCourse"))
#
#
# testsuite.addTests(unittest.makeSuite(Teacher4TestCase))
#
# run = BeautifulReport(testsuite)
# #run.report(filename='教师端测试报告2'+now+'.html', description='备课系统测试', log_path='.')
# #run.report(filename='教师端测试报告2'+now+'.html', description='备课系统测试', report_dir='report')
# # mac 路径
# run.report(filename='教师端测试报告.html', description='备课系统测试', report_dir='/Users/shuping/.jenkins/workspace/autotest')
# # linux 路径
# #run.report(filename='教师端测试报告.html', description='备课系统测试', report_dir='/usr/local/python3/Testreport')
#
#
# # 下面是HTMLTestRunner执行的测试报告
# # filename = "/Users/shuping/.jenkins/workspace/autotest/Treport.html"  # 定义个报告存放路径，支持相对路径 mac路径
# # #filename = "/usr/local/python3/Testreport/Treport.html"  # 定义个报告存放路径，支持相对路径 linux路径
# # f = open(filename, 'wb')  # 结果写入HTML 文件
# # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='suping的自动化测试报告', description='用例执行情况：')
# # runner.run(testsuite)
# # f.close()
run.report(filename='教师端测试报告.html', description='备课系统测试', report_dir='/Users/shuping/.jenkins/workspace/autotest')
# linux 路径
#run.report(filename='教师端测试报告.html', description='备课系统测试', report_dir='/usr/local/python3/Testreport')


# 下面是HTMLTestRunner执行的测试报告
# filename = "/Users/shuping/.jenkins/workspace/autotest/Treport.html"  # 定义个报告存放路径，支持相对路径 mac路径
# #filename = "/usr/local/python3/Testreport/Treport.html"  # 定义个报告存放路径，支持相对路径 linux路径
# f = open(filename, 'wb')  # 结果写入HTML 文件
# runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='suping的自动化测试报告', description='用例执行情况：')
# runner.run(testsuite)
# f.close()