from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('D:/test/环境配置/HTML/checkbox.html') #url
driver.get(file_path) #向浏览器输入网址，打开页面
# 选择页面上所有的input，然后从中过滤出所有的checkbox 并勾选
inputs = driver.find_elements_by_tag_name('input') #获取一组元素
for puts in inputs:#循环遍历
    if puts.get_attribute('type') == 'checkbox': #if判断
        puts.click()
time.sleep(6)
driver.quit()