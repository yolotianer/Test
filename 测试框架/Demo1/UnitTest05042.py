import unittest
from selenium import webdriver
import time
from ddt import ddt, data, unpack

# 读取文件
def readFile():
    # 定义一个list集合
    params=[]
    # 打开文件
    # file=open('params.txt')：错误
    file=open('params.txt','r',encoding='UTF-8')
    # 读取文件，先读取所有行，再处理每一行
    for line in file.readlines():
        # strip('\n')：去掉换行'\n'
        params.append(line.strip('\n').split('，'))
    file.close()
    return params

#在类之前引入ddt装饰器，证明你在这个类中需要用到ddt
@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # self.driver.get("http://www.baidu.com")

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()

    # def test_baidu1(self):
    #     self.driver.find_element_by_id("kw").send_keys("肖战")
    #     self.driver.find_element_by_id("su").click()
    # def test_baidu2(self):
    #     self.driver.find_element_by_id("kw").send_keys("小龙女")
    #     self.driver.find_element_by_id("su").click()

    @data(*readFile())
    @unpack
    def test_baidu(self,url,txt):
        self.driver.get(url)
        self.driver.find_element_by_id("kw").send_keys(txt)
        self.driver.find_element_by_id("su").click()


    # @data(('肖战', '小龙女'), ('秦牛正威', '二哈'))
    # @unpack
    # def test_print(self,txt1,txt2):
    #     print(txt1)
    #     print(txt2)

    @data(*readFile())
    @unpack
    def test_print(self,txt1,txt2):
        print(txt1)
        print(txt2)

if __name__ == '__main__':
    unittest.main()
