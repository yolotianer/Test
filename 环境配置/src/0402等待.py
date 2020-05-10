#学习：https://blog.csdn.net/sinat_41774836/article/details/88965281
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("肖战")
driver.find_element_by_id("su").click()
#添加等待:
# 强制等待:time.sleep(10)
# 隐式等待:driver.implicitly_wait(10)
# 显示等待
WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_link_text("肖战_百度百科"))
driver.find_element_by_link_text("肖战_百度百科").click()
time.sleep(10)
driver.quit()
