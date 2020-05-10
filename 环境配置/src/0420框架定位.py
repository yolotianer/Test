from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath('D:/test/环境配置/HTML/frame.html')
driver.get(file_path)
driver.implicitly_wait(30)
#先找到ifrome1(id=1)
# <iframe id="f1" src="inner.html" width="800" ,="" height="600"></iframe>
driver.switch_to.frame("f1")
#<iframe id="f2" src="http://www.baidu.com" width="700" height="500"></iframe>
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("山有木兮木有枝，心悦君兮君不知")
# send_keys(Keys.ENTER)  回车
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()