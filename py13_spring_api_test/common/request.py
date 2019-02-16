import requests
from common.config import ReadConfig
from common.my_log import my_log



class Request:
    def __init__(self):
        self.session = requests.Session()
        self.mylog = my_log('request')

    def request(self,method,url, data = None):
        method =method.upper()
        url = ReadConfig().get_value('URL','pre_url') +url
        self.mylog.info('url:'.format(url))
        self.mylog.info('data:{}'.format(data))
        if data is not None and type(data)== str:
            data = eval(data)   #如果data是字符串，转换成字典
        if method =='GET':
            resp = self.session.request(method=method, url=url, params=data)
            self.mylog.info('response:{}'.format(resp.text))
            return resp
        elif method =='POST':
            resp = self.session.request(method=method, url=url, data=data)
            self.mylog.info('response:{}'.format(resp.text))
            return resp
        else:
            self.mylog.info('Un-supported method !!!')


if __name__ == '__main__':
    re =Request()
    re.request('post','member/login',{"mobilephone": "13544189428", "pwd": "123456"})
    re.request('post','member/bidLoan',{"memberId": 2622, "pwd": "123456","loanId": 146,"amount" :500})