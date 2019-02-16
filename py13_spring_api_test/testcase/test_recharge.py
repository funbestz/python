from common.request import Request
from common.do_excel import DoExcel
from common import constant
import unittest
from ddt import ddt,data
from common.my_log import my_log
from common.config import ReadConfig


@ddt
class TestRecharge(unittest.TestCase):
    '这是一个充值接口测试类'
    do_excel = DoExcel(constant.case_file)
    cases_recharge = do_excel.read_data('recharge')
    mylog = my_log('recharge')

    @classmethod
    def setUpClass(cls):
        cls.request = Request()


    # def setUp(self):
    #     self.mylog.info('------------------------------开始执行用例--------------------------')

    @data(*cases_recharge)
    def test_recharge(self, case):  # 测试充值
        self.mylog.info('开始执行第{}条用例'.format(case.case_id))
        resp = self.request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.json()['msg'])
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'FAIL'
            raise e
        finally:
            self.do_excel.write_back(case.case_id + 1, resp.text, TestResult)  # 写回实际结果
            self.mylog.info('第{}条用例的执行结果是{}'.format(case.case_id, TestResult))

    # def tearDown(self):
    #     self.mylog.info('------------------------------用例执行完成--------------------------')

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()


if __name__ == '__main__':
    unittest.main()




