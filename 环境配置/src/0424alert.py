from selenium import webdriver
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("D:/test/环境配置/HTML/alert.html")
driver.get(file_path)
driver.find_element_by_id("tooltip").click()
time.sleep(3)
alert = driver.switch_to.alert
# alert.accept()接受
# text = alert.text返回文本内容
# print(text)
#alert.dismiss()取消
time.sleep(2)
driver.quit()

