import unittest
from ddt import file_data,ddt
from selenium import webdriver
import time

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()

    @file_data('baidu.yml')

    def test_1(self,**kwargs):
        # 获取kwargs集合中，key url，text的value
        self.driver.get(kwargs.get('url'))
        self.driver.find_element_by_id('kw').send_keys(kwargs.get('text'))
        self.driver.find_element_by_id('su').click()




if __name__ == '__main__':
    unittest.main()
