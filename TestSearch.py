# encoding=utf-8
'''
百度搜索温一壶清酒
'''

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: TestSearch
@time: 2020-05-03 22:16
@desc:
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from pages.SearchPage import SearchPage
import config.config as cf
from common.mainModule import log
import time
from common.mail import Email
from common.ExcelList import ExcelList
from common.ExcelData import ExcelData
import allure
import common.ReportZip as report_zip
import common.Argprase as argparse
from pages.JenkinsPage import JenkinsPage

# test_data = [
#     # 测试数据
#     {
#         "case": "正确断言",
#         "keywords": "温一壶清酒 博客园",
#         "assert": "温一壶清酒 博客园_百度搜索",
#         "expected": {"msg": "断言成功", "data": None}
#     },
#     {
#         "case": "异常断言",
#         "keywords": "温一壶清酒 博客园",
#         "assert": "温一壶清酒 博客园",
#         "expected": {"msg": "断言失败", "data": None}
#     }
# ]
#
# log.info('配置初始化')
# cf.init()
ed = ExcelData()
el = ExcelList()


class TestSearch():
    @allure.step("搜索测试")
    @allure.feature("百度搜索测试")
    @allure.story("温一壶清酒 执行")
    @allure.severity("trivial")
    @pytest.mark.mock
    @pytest.mark.parametrize('data', ed.get_excel_datas(), ids=el.get_ids())
    def test_case01(self, quit_driver, data):
        '''
        搜索测试
        '''
        sp = SearchPage()
        # sp.test_search(keyword=sp.get_excel_datas()[0]['操作输入值'])
        # assert sp.op_title() == sp.get_excel_datas()[0]['断言']
        log.info(ed.get_excel_datas())
        log.info(el.get_ids())
        log.info(data['操作输入值'])
        sp.test_search(keyword=data['操作输入值'])
        assert sp.op_title() == data['断言']
        log.info(sp.op_title())

    @pytest.mark.jenkins
    def test_case02(self, quit_driver):
        '''
        jenkins
        '''
        jp = JenkinsPage()
        jp.login_success('a', 'a')


if __name__ == '__main__':
    arg = argparse.Argprase()
    arg.get_args()
    # log.info('配置初始化')
    # cf.init()
    log.info('主程序中获取到的site地址：' + cf.get_value('site'))
    log.info('开始运行代码')
    report_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_name = 'search' + report_time + '.html'
    # pytest.main(['-q', '-s', 'TestSearch.py', '-m mock'])  # mock标记测试
    # 生成html报告
    # pytest.main(['-q', '-s', 'TestSearch.py', '--reruns', '1', '--html=./report/' + report_name , '--self-contained-html'])
    # 生成allure报告
    mark = cf.get_value('mark')
    log.info('获取到的mark数据：' + mark)
    pytest.main(['-q', '-s', 'TestSearch.py', '-m' + mark, '--alluredir', '/var/jenkins_home/workspace/github_demo/allure-report'])
    # init_report = 'allure generate --clean ./report'
    # os.system(init_report)
    # log.info("测试报告json文件初始化成功！")
    time.sleep(2)
    # report_file_path = os.getcwd() + '\\allure - report'
    # report_zip_path = os.getcwd() + '\\reportzip\\' + '自动化测试' + report_time + '.zip'
    # report_file_path = '/var/jenkins_home/workspace/github_demo/target/allure-results'
    # report_zip_path = '/var/jenkins_home/workspace/github_demo/reportzip/' + '自动化测试' + report_time + '.zip'
    # # 调用打包程序
    # data = report_zip.ReportZip(report_file_path, report_zip_path)
    # data.report_zip()
    # del_report_path = 'del /f /q G:\\202001-202012\\pytest\\Pytest_Auto_Test\\report'
    # log.info(del_report_path)
    # os.system(del_report_path)
    # log.info("删除report下的json文件")
    # mail_msg = """
    #             <p>Python 邮件发送测试...</p>
    #             <p><a href="https://www.cnblogs.com/hong-fithing/">这是温一壶清酒的博客链接</a></p>
    #     """
    # # 调用邮件
    # e = Email(title='百度搜索测试报告', message=mail_msg, receiver='',
    #           server='', sender='',
    #           password='',
    #           path='./report/' + report_name
    #           )
    # log.info("调用邮件")
    # e.send()
    # log.info("邮件发送成功")