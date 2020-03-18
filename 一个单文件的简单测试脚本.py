import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
from selenium import webdriver
--------------------------------设置类名，初始化类
class TestAuto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
---------------------------------案例初始化脚本，简单的元素定位方法，八大方法可百度查看用法进行学习。简单的登录单元测试用例。time.sleep(1)
self.driver.get('http://yingxiao.xuanwo001.com')
# self.driver.find_element_by_class_name('el-checkbox__inner').click()  # 勾选不再提示
# time.sleep(1)
# self.driver.find_element_by_xpath('//*[@id="main-content"]/div/div[7]/div/i').click()  # 关闭活动页面
# time.sleep(1)
self.driver.find_element_by_class_name('main-btn').click()  # 点击触发登录按钮
time.sleep(1)
self.driver.find_element_by_xpath(
    '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/h3/button[2]').click()  # 点击切换到密码登录
time.sleep(1)
self.driver.find_element_by_xpath(
    '//*[@id="app"]/div[2]/div[1]/div/div[2]/form/div[1]/div/div/input').send_keys('手机号')
time.sleep(1)
self.driver.find_element_by_xpath(
    '//*[@id="app"]/div[2]/div[1]/div/div[2]/form/div[2]/div/div/input').send_keys('密码')
time.sleep(1)
self.driver.find_element_by_class_name('login-btn').click()  # 点击登录
print u'-------------------------------The test case Running start >>'
---------------------------------------------测试用例名设置，以及设计用例title、设置断言
def testCase_001(self):
    '''验证网址打开是否正确测试用例'''
    print u'test_001>正常打开网址进入旋涡首页'
    self.assertEqual('https://yingxiao.xuanwo001.com/#/index', self.driver.current_url)
    print u'>>>PASS'
....多个用例
-------------------------------------------结束用例
def tearDown(self):
    self.driver.quit()
    print u'--------------------------------The test case End of Run >>'
---------------------------------------------------------------将测试用例集合if __name__ == '__main__':
    # unittest.mian()
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestAuto("testCase_001"))
    suiteTest.addTest(TestAuto("testCase_002"))
    suiteTest.addTest(TestAuto("testCase_003"))
--------------------------------------------------------------生成测试报告的路径、名称。描
# 按照一定时间格式获取当前时间(防止测试报告覆盖)now = time.strftime(u'%Y-%m-%d-%H-%M-%S')
# 确定生成报告的路径
report_file = "D:\\python+selenium\\report\\" + now + "_test_report.html"
with open(report_file, 'wb') as report:
    runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=u'title',
                                           description=u'描述',
                                           tester=u'测试人员')
    # runner = unittest.TextTestRunner()
    runner.run(suiteTest)
    report.close(
————————————————
版权声明：本文为CSDN博主「tester_sc」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/tester_sc/article/details/81135448