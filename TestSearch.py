'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: TestSearch
@time: 2020-05-03 22:16
@desc:
'''

from selenium import webdriver
import pytest
import time


class TestSearch():

    def test_case01(self):
        keyword = '温一壶清酒 博客园'
        url = 'https://www.baidu.com'
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.find_element_by_id('kw').send_keys(keyword)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-q', '-s', 'TestSearch.py'])