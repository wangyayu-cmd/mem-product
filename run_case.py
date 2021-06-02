# -*- coding: utf-8 -*-

import unittest
import datetime
from BeautifulReport import BeautifulReport

test_suite = unittest.defaultTestLoader.discover('./case', pattern='test*.py')
result = BeautifulReport(test_suite)
# now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
# filename = '测试报告' + str(now)
filename = '产品库测试报告'
result.report(filename=filename, description='产品库测试报告', log_path='./report')

