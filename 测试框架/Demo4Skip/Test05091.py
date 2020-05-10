import unittest


class MyTestCase(unittest.TestCase):
    # 无条件跳过
    @unittest.skip('不想运行')
    def test_print1(self):
        print(1)

    # 有条件跳过
    @unittest.skipIf(1<2,'这是if的理由,且if条件为true，则跳过该用例的执行')
    def test_print2(self):
        print(2)
    @unittest.skipUnless(1>2,'这是if的理由,且if条件为false，则跳过该用例的执行')
    def test_print3(self):
        print(3)

    # 如果用例执行失败，则不计入失败的case数
    # 会出现出错提示，不过不抛出红色字体的异常，也不会计入日志，4，5可以对比来看
    @unittest.expectedFailure
    def test_print4(self):
        print(4)
        self.assertEqual(3,4,msg='not equal')

    def test_print5(self):
        print(5)
        self.assertEqual(3, 4, msg='not equal')


if __name__ == '__main__':
    unittest.main()
