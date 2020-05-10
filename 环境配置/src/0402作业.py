#网易邮箱账户名和密码登陆
from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.get("https://mail.163.com/")
driver.find_element_by_id("switchAccountLogin").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input").send_keys("18821769219")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]").send_keys("mmwan980815")
driver.find_element_by_link_text("登陆").click()
time.sleep(30)
driver.quit()