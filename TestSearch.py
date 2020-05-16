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
from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    cf.set_value('driver', driver)
    log.info('驱动信息：' + str(cf.get_value('driver')))


class TestSearch:

    def test_case01(self):
        sp = SearchPage(driver=cf.get_value('driver'))
        sp.test_search(keyword='温一壶清酒 博客园')
        assert sp.op_title() == '温一壶清酒 博客园_百度搜索'
        log.info(sp.op_title())
        sp.quit()

    def test_case02(self):
        sp1 = SearchPage(driver=cf.get_value('driver'))
        sp1.test_search(keyword='温一壶清酒')
        assert sp1.op_title() == '温一壶清酒 博客园'
        log.info(sp1.op_title())
        sp1.quit()


if __name__ == '__main__':
    log.info('配置初始化')
    cf.init()
    log.info('开始运行代码')
    main()
    pytest.main(['-q', '-s', 'TestSearch.py'])