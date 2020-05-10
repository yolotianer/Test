import unittest
from Demo1.forTest import *
import os
import datetime
from HTMLTestRunner import HTMLTestRunner
suite=unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(forTest))

report_path='./report'
report_file='report.html'

if not os.path.exists(report_path):
    os.mkdir(report_path)
with open(report_file,'wb')as report:
    runner=unittest.TextTestRunner()
    runner.run(suite)