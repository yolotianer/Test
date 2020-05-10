import unittest
from Demo4Skip.Test05091 import *

# 创建一个测试套件=list
suit=unittest.TestSuite()

# 添加测试用例(子元素)到测试套件（集合）
# # 方式一：单个依次添加
# suit.addTest(MyTestCase('test_print1'))
# suit.addTest(MyTestCase('test_print5'))
# suit.addTest(MyTestCase('test_print4'))

# 方式二：批量添加，通过集合
case=[MyTestCase('test_print1'),MyTestCase('test_print5'),MyTestCase('test_print4')]
suit.addTests(case)

# 套件通过TextTestRunner对象进行运行=unittest.main()
runner=unittest.TextTestRunner()
runner.run(suit)