#环境搭建
import unittest

#通过继承unittest.TestCase来实现测试用例
class forTest (unittest.TestCase):
    #类的初始化和释放,利用@classmethod可以正常使用，否则会报错
    @classmethod
    def setUpClass(cls) -> None:
        print('class')
    @classmethod
    def tearDownClass(cls) -> None:
        print('class')
    #初始化
    def setUp(self) -> None:
        print('setUp')
    #释放
    def tearDown(self) -> None:
        print('tearDown')
    #测试用例1
    def test_a(self):
        print('a')

    #测试用例2
    def test_b(self):
        print('b')

    #普通方法，不会被 unittest识别，除非自己调用，否则不会产生任何作用
    def plus(self,a,b):
        print(a+b)
        return a+b
    #测试用例3,在测试用例里调用普通方法
    def test_c(self):
        self.plus(1,2)

if __name__ == '__main__':
        unittest.main()


