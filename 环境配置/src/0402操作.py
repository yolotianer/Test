from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
data=driver.find_element_by_name("tj_trnews").text
print(data)
time.sleep(5)
driver.quit()
