import HTMLTestRunnerNew
import unittest
from testcase.test_register import TestRegister
from testcase.test_recharge import TestRecharge
from testcase.test_login import TestLogin
from common import constant

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
#
# suite.addTest(loader.loadTestsFromTestCase(TestRegister))
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))
# suite.addTest(loader.loadTestsFromTestCase(TestRecharge))
discover = unittest.defaultTestLoader.discover(constant.testcase_dir, pattern ='test_*.py',top_level_dir=None)

with open(constant.report_file, "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title="测试报告",description="测试前程贷项目接口",tester="spring")
    runner.run(discover)
