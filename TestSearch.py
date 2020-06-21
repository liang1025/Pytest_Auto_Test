'''
测试搜索温一壶清酒
'''

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: TestSearch
@time: 2020-05-03 22:16
@desc:
'''

import pytest
from pages.SearchPage import SearchPage
import config.config as cf
from common.mainModule import log
import time
from common.mail import Email


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
# ids = [
#     "测试：{}->输入值:{}-断言值:{}-预期:{}".
#         format(data["case"], data["keywords"], data["assert"], data["expected"]) for data in test_data
# ]


class TestSearch():
    @pytest.mark.mock
    # @pytest.mark.parametrize('data', test_data, ids=ids)
    def test_case01(self, quit_driver):
        '''
        正常断言case
        '''
        sp = SearchPage()
        sp.test_search(keyword=sp.datas[1]['操作输入值'])
        assert sp.op_title() == sp.datas[1]['断言']
        log.info(sp.op_title())

    def test_case02(self, quit_driver):
        '''
        异常断言case
        '''
        sp1 = SearchPage()
        sp1.test_search(keyword=sp1.datas[1]['操作输入值'])
        assert sp1.op_title() == sp1.datas[1]['断言']
        log.info(sp1.op_title())


if __name__ == '__main__':
    log.info('配置初始化')
    cf.init()
    log.info('开始运行代码')
    report_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_name = 'search' + report_time + '.html'
    # pytest.main(['-q', '-s', 'TestSearch.py', '-m mock'])  # mock标记测试
    pytest.main(['-q', '-s', 'TestSearch.py', '--reruns', '1', '--html=./report/' + report_name , '--self-contained-html'])
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