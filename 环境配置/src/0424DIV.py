import os
import time
from selenium import webdriver
driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("D:/test/环境配置/HTML/DIV.html")
driver.get(file_path)
time.sleep(3)
driver.find_element_by_id("show_modal").click()
time.sleep(3)
driver.find_element_by_id("click").click()
time.sleep(3)
#如果页面只有一组button时，可以通过button直接定位
elements = driver.find_elements_by_tag_name("button")
#不止一组button的时候，可以先定位div,再去定位，也就是先定位外出，在定位内层
#buttons =dr.find_element_by_class_name('modal-footer').find_elements_by_tag_name('button')
elements[0].click()
driver.quit()