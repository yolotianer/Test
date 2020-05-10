import os
import time
from selenium import webdriver
driver=webdriver.Chrome()
file_path = "file:///"+os.path.abspath("D:/test/环境配置/HTML/send.html")
driver.get(file_path)
driver.maximize_window()
driver.find_element_by_xpath("//*[@value='请点击']").click()
#如何找alert中的输入框
alert = driver.switch_to.alert
#输入内容
alert.send_keys("郭小天")
time.sleep(3)
#再次接受，进行确认
alert.accept()
time.sleep(3)
driver.quit()