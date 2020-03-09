#切换句柄handle，用于页面跳转后无法定位的情况
#获取当前页句柄
main_windows = driver.current_window_handle
print(main_windows)
#切换句柄
all_windows = driver.window_handles
print(all_windows)

for handle in all_windows:
    if handle != main_windows:
        driver.switch_to.window(handle)

register_windows = driver.current_window_handle
print(register_windows)


########################################################################################

#切换iframe/frame，常用在页面未发生改变，在检查中可以找到元素，但是却无法正常定位和触发
driver.switch_to.frame("id")
#此处id可以换位name，直接填写，不用指向某个名称
driver.switch_to.frame(driver.find_element_by_xpath("XXXXXXXXXXXX"))
#用webelement来定位

#从frame中切回主文档(switch_to.default_content())
driver.switch_to.default_content()


#frame嵌套，一级一级切下去
driver.switch_to.frame("父")
driver.switch_to.frame("子")
#切回父frame
driver.switch_to.parent_frame()


