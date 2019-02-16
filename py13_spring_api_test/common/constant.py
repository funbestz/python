import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir,'datas')
case_file = os.path.join(data_dir,'case.xlsx')
conf_dir = os.path.join(base_dir,'conf')
globle_file = os.path.join(conf_dir,'globle.conf')
conf_file = os.path.join(conf_dir,'config.conf')
conf_file2 = os.path.join(conf_dir,'config2.conf')
report_dir = os.path.join(base_dir,'reports')
report_file = os.path.join(report_dir,'Report.html')
log_dir = os.path.join(base_dir,'logs')
log_file = os.path.join(log_dir,'my_logger.log')
testcase_dir = os.path.join(base_dir,'testcase')

