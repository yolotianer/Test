from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("D:/test/环境配置/HTML/drop_dwon.html")
driver.get(file_path)
ship1=driver.find_element_by_id("ShippingMethod")
ship1.find_element_by_xpath("//*[@value='10.69']").click()
time.sleep(6)

ship2=driver.find_element_by_id("ShippingMethod")
ship2.find_element_by_xpath("//option[@value='11.61']").click()
time.sleep(6)
driver.quit()
