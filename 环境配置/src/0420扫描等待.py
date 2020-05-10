from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import os


driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath('D:/test/环境配置/HTML/level_locate.html')
driver.get(file_path)
#点击Link1链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()
WebDriverWait(driver,10).until(lambda the_driver: driver.find_element_by_id("dropdown1"))
lists_element = driver.find_element_by_id("dropdown1").find_element_by_link_text("Action")
ActionChains(driver).move_to_element(lists_element).perform()
time.sleep(6)
driver.quit()