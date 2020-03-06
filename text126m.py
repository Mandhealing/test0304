from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


#打开浏览器并进入‘网易云音乐'
driver = webdriver.Chrome()       
driver.maximize_window()
driver.get('https://music.163.com/')
driver.implicitly_wait(10)
#sleep(5)


#点击登录按钮
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/a').click()
#sleep(2)


#选中同意协议的复选框
checkboxs = driver.find_element_by_xpath(".//*[@type='checkbox']")
checkboxs.click()
#sleep(2)


#选择通过网易账户登录
stepto_login = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/ul/li[4]/a')
stepto_login.click()
#sleep(3)

#录入用户名，密码
send_id = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[1]/input')
send_id.clear()
#sleep(1)
send_id.send_keys('wxlbuy@126.com')
#sleep(3)


send_pw = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[2]/input')
send_pw.clear()
#sleep(1)
send_pw.send_keys('Wxl880615')
currentWin = driver.current_window_handle  # 获取当前窗口handle name
handles = driver.window_handles
#sleep(5)


#点击登录按钮完成登录
login_log = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[7]/a')
login_log.click()
#sleep(5)

#签到
#day_check = driver.find_element_by_xpath("//div[@class='f-cb']/div/div/a")
#day_check = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/div/div/a")
#day_check.click()
#sleep(2)

for i in handles:
    if currentWin == i:
        continue
    else:
        #将driver与新的页面绑定起来
        driver = driver.switch_to.window(i)

#进入每日推荐
day_good = driver.find_element_by_xpath("//p[@class ='dec']/a[@title='每日歌曲推荐']")
#ActionChains(driver).move_to_element(day_good).perform()
day_good.click()


#

#




# 退出IE浏览器
#def tearDown(self):
        #self.driver.quit()






