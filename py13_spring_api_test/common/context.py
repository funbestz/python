import re
from common.config import ReadConfig
config = ReadConfig()
class Context:
    admin_user = config.get_value('data','admin_user')
    admin_pwd = config.get_value('data','admin_pwd')
    loan_member_id = config.get_value('data','loan_member_id')
    normal_user = config.get_value('data', 'normal_user')
    normal_pwd = config.get_value('data', 'normal_pwd')
    normal_member_id = config.get_value('data', 'normal_member_id')

def replace(str,dict):
    p = "\$\{(.*?)}"
    while re.search(p,str):
        m = re.search(p,str)
        key = m.group(1)
        value = dict[key]
        str = re.sub(p,value,str,count= 1)
    return str
def replace_new(str):
    p = "\$\{(.*?)}"
    while re.search(p,str):
        m = re.search(p,str)
        key = m.group(1)
        if hasattr(Context,key):
            value = getattr(Context,key)  #利用反射，动态获取属性
            str = re.sub(p,value,str,count= 1)
        else:
            return None
    return str

if __name__ == '__main__':
    s ='{"mobilephone":"${admin_user}", "pwd": "${admin_pwd}"}'
    data = {"admin_user":"15873171553","admin_pwd":"123456"}
    print(replace(s,data))
    s = replace_new(s)
    print(s)