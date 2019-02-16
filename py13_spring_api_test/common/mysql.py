import pymysql
from common.config import ReadConfig

class MysqlUtil:
    def __init__(self):
        config = ReadConfig()
        host = config.get_value('DB','host')
        user = config.get_value('DB','user')
        pwd = config.get_value('DB','pwd')
        self.mysql = pymysql.connect(host=host, user=user, password=pwd, port=3306)  # 连接数据库
        self.cursor = self.mysql.cursor()  # 获取操作游标
    def fetch_one(self,sql):
        self.cursor.execute(sql) #执行SQL语句
        result = self.cursor.fetchone()
        return result

    def close(self):
        self.cursor.close()  # 关闭查询
        self.mysql.close()  # 关闭连接

if __name__ == '__main__':
    mysql = MysqlUtil()
    sql = "select * from future.member where Type = 1"
    member_id = mysql.fetch_one(sql)[0]
    sql2 = "select * from future.loan where memberId = @member_id"
    result = mysql.fetch_one(sql2)  # 返回的是tuple
    print(result)  # 使用下标去获取值
    mysql.close()

