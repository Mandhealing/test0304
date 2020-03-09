from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()       
driver.maximize_window()
driver.get('https://www.jianshu.com/p/69af30fd5f6b')
driver.implicitly_wait(10)


main_windows = driver.current_window_handle
print(main_windows)


#点击登录按钮
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/aside/div/div/section[1]/div[1]/div[1]/a').click()
#sleep(2)

all_windows = driver.window_handles
print(all_windows)

for handle in all_windows:
    if handle != main_windows:
        driver.switch_to.window(handle)


register_windows = driver.current_window_handle
print(register_windows)
