from common.request import Request
from common.do_excel import DoExcel
from common import constant
import unittest
from libExt.ddtnew import ddt,data
from common.config import ReadConfig
import json
from common.mysql import MysqlUtil
from common import context
from common.mysql import MysqlUtil
from common.my_log import my_log

@ddt
class TestInvest(unittest.TestCase):
    '这是一个投资接口测试类'
    do_excel = DoExcel(constant.case_file)
    cases_invest = do_excel.read_data('invest')
    mylog = my_log('invest')


    @classmethod
    def setUpClass(cls):
        cls.request = Request()
        cls.mysql = MysqlUtil()

    # def setUp(self):
    #     self.mylog.info('------------------------------开始执行用例--------------------------')

    @data(*cases_invest)
    def test_invest(self, case):  #测试投资
        self.mylog.info('开始执行第{}条用例'.format(case.case_id))
        #查找参数化测试数据，动态替换
        case.data = context.replace_new(case.data)
        resp = self.request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.json()['msg'])
            TestResult = 'PASS'
            if resp.json()['msg'] == "加标成功":
                loan_member_id = getattr(context.Context,'loan_member_id')
                sql = "select id from future.loan where memberID = {} order by createTime desc limit 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(context.Context,'loan_id',str(loan_id))
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
        cls.mysql.close()

if __name__ == '__main__':
    unittest.main()




