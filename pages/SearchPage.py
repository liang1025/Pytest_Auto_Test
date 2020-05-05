'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: SearchPage
@time: 2020-05-04 20:08
@desc:
'''

from pages.BasePage import BasePage
from selenium import webdriver
import config.config as cf


class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    input_keyword = 'id,kw'
    click_enter = 'id,su'

    keyword = '温一壶清酒 博客园'
    url = 'https://www.baidu.com'

    def input_key(self):
        self.send_key(self.input_keyword, self.keyword)

    def click_search(self):
        self.click(self.click_enter)

    def test_search(self):
        self.open(url=self.url)
        self.input_key()
        self.click_search()
        self.sleep(2)
        self.quit()