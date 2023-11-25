from BSTestRunner import BSTestRunner
import unittest

testcases='./test_cases'
discover=unittest.defaultTestLoader.discover(testcases,'test*.py')
reportname='./test_reports/'+'report'+'.html'
with open(reportname,'wb') as f:
    runner=BSTestRunner(stream=f, title='测试报告', description='测试报告明细')
    runner.run(discover)
f.close()