from configparser import ConfigParser
from common import constant

class ReadConfig:

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(constant.globle_file,encoding='utf-8')
        open = self.cf.getboolean('SWITCH', 'open')
        if open:
            self.cf.read(constant.conf_file, encoding='utf-8')
        else:
            self.cf.read(constant.conf_file2,encoding='utf-8')
    def get_value(self,section, option):
        return eval(self.cf.get(section,option))
    def get_boolen(self,section, option):
        return eval(self.cf.getboolean(section,option))

if __name__ == '__main__':
    print(ReadConfig().get_value('URL', 'pre_url'))