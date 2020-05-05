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
        sp.test_search()


if __name__ == '__main__':
    log.info('配置初始化')
    cf.init()
    log.info('开始运行代码')
    main()
    pytest.main(['-q', '-s', 'TestSearch.py'])