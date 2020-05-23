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


class TestSearch:
    def test_case01(self, quit_browser):
        sp = SearchPage()
        sp.test_search(keyword='温一壶清酒 博客园')
        assert sp.op_title() == '温一壶清酒 博客园_百度搜索'
        log.info(sp.op_title())

    def test_case02(self, quit_browser):
        sp1 = SearchPage()
        sp1.test_search(keyword='温一壶清酒')
        assert sp1.op_title() == '温一壶清酒 博客园'
        log.info(sp1.op_title())


if __name__ == '__main__':
    log.info('配置初始化')
    cf.init()
    log.info('开始运行代码')
    pytest.main(['-q', '-s', 'TestSearch.py'])