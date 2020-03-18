from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


file_name = "myaccount.txt"
dataset = []

file = open(file_name, mode='r')
for line in file:
    line = line.split()
    dataset.append(line)



#list_name = input('今日歌单名')
now_day = time.strftime("%Y/%m/%d")
list_name = '每日歌单推荐---' + now_day


#打开浏览器并进入‘网易云音乐'
driver = webdriver.Chrome()       
driver.maximize_window()
driver.get('https://music.163.com/')
driver.implicitly_wait(10)


#点击登录按钮
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/a').click()


#选中同意协议的复选框
checkboxs = driver.find_element_by_xpath(".//*[@type='checkbox']")
checkboxs.click()


#选择通过网易账户登录
stepto_login = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/ul/li[4]/a')
stepto_login.click()


#录入用户名，密码
send_id = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[1]/input')
send_id.clear()
send_id.send_keys(dataset[0])


send_pw = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[2]/input')
send_pw.clear()
send_pw.send_keys(dataset[1])


#点击登录按钮完成登录
login_log = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[7]/a')
login_log.click()

#切换frame后继续定位，不切换无法正常定位和触发
driver.switch_to.frame("g_iframe")


#签到
day_check = driver.find_element_by_xpath("//div[@class='f-cb']/div/div/a")
#day_check = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/div/div/a")
day_check.click()


#展示出每日推荐栏（否则会有播放器组件的遮挡）
driver.execute_script("window.scrollBy (0,800);")


#进入每日推荐
day_good = driver.find_element_by_xpath("//p[@class ='dec']/a[@title='每日歌曲推荐']")
#day_good = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/ul/li[1]/a")
day_good.click()


add_all = driver.find_element_by_xpath("//*[@class ='u-btni u-btni-fav f-fl']")
add_all.click()


#driver.switch_to.frame("g_iframe")
create_newlist0 = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]")
create_newlist0.click()

create_newlist1 = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/p[1]/input").send_keys(list_name)
create_newlist2 = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[2]/a[1]")
create_newlist2.click()



#退出IE浏览器
def tearDown(self):
        self.driver.quit()