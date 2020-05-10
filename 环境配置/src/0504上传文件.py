from selenium import webdriver
import time
import os
driver=webdriver.Chrome()
file_path="file:///"+os.path.abspath("D:/test/环境配置/HTML/upload.html")
driver.get(file_path)
driver.implicitly_wait(10)#智能等待
driver.find_element_by_name("file").send_keys("C:/Users/24713/Desktop/画图/2019072318262051.png")
time.sleep(8)#固定等待
driver.quit()