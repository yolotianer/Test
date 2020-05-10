import unittest
from  selenium import webdriver
import time
from ddt import ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):
    @file_data('ppp.yml')
    def test_print(self,**kwargs):
        name=kwargs.get('name')
        print(name)
        age=kwargs.get('age')
        print(age)
        self.assertEqual(name,'郭天',msg='not equal')



if __name__ == '__main__':
    unittest.main()
