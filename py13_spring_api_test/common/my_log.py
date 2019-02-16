import logging
from common.config import ReadConfig
from common import constant

def my_log(log_name):
    config = ReadConfig()
    log_level = config.get_value('LOG', 'log_level')   #从配置文件中读取日志级别
    console_level = config.get_value('LOG', 'console_level') #从配置文件读取控制台输出级别
    file_level = config.get_value('LOG', 'file_level')  #日志存放文件中的级别
    formatter = config.get_value('LOG', 'formatter') #从配置文件读取输出格式
    log_file = constant.log_file  #获取log文件存放路径

    my_logger = logging.getLogger(log_name)  #创建一个日志收集器
    my_logger.setLevel(log_level)

    formatter = logging.Formatter(formatter)
    ch = logging.StreamHandler()
    ch.setLevel(console_level)
    ch.setFormatter(formatter)

    fh = logging.FileHandler(log_file,encoding='utf-8')
    fh.setLevel(file_level)
    fh.setFormatter(formatter)

    my_logger.addHandler(ch)
    my_logger.addHandler(fh)
    return my_logger


if __name__ == '__main__':
   log = my_log('register')
   log.info('dddddddd')
