from common.request import Request
from common.do_excel import DoExcel
from common import constant
from common.mysql import MysqlUtil
import unittest
from ddt import ddt,data
from common.config import ReadConfig
import json
from common.my_log import my_log
from common import context
from common.context import Context


@ddt
class TestRegister(unittest.TestCase):
    '这是一个注册接口测试类'
    do_excel = DoExcel(constant.case_file)
    cases_register = do_excel.read_data('register')
    mylog = my_log('register')

    @classmethod
    def setUpClass(cls):
        cls.request = Request()
        cls.mysql = MysqlUtil()

    # def setUp(self):
    #     self.mylog.info('------------------------------开始执行用例--------------------------')
    @data(*cases_register)
    def test_register(self,case): #测试注册接口
        self.mylog.info('开始执行第{}条用例'.format(case.case_id))
        # data = json.loads(case.data)
        sql = "select max(mobilephone) from future.member"
        register_number = int(self.mysql.fetch_one(sql)[0]) + 1
        setattr(Context, 'register_number', str(register_number))
        case.data = context.replace_new(case.data)
        resp = self.request.request(case.method,case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.text)
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'FAIL'
            raise e
        finally:
            self.do_excel.write_back(case.case_id+1,resp.text,TestResult) #写回实际结果
            self.mylog.info('第{}条用例的执行结果是{}'.format(case.case_id,TestResult))
    # def tearDown(self):
    #     self.mylog.info('------------------------------用例执行完成--------------------------')
    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()
        cls.mysql.close()


if __name__ == '__main__':
    unittest.main()




