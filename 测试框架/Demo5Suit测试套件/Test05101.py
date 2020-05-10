import unittest
from Demo1.forTest import *
# 方式三:通过搜索py文件
# test_dir= '/Demo1'
# discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='Unit*.py')
# runner=unittest.TextTestRunner()
# runner.run(discover)

# 方式四：
suite=unittest.TestSuite()
# 4.1
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(forTest))
# 4.2
# suite.addTests(unittest.TestLoader().loadTestsFromName('Demo1.forTest.forTest'))
runner=unittest.TextTestRunner()
runner.run(suite)