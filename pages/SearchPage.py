'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: SearchPage
@time: 2020-05-04 20:08
@desc:
'''

from pages.BasePage import BasePage
from common.mainModule import log


class SearchPage(BasePage):
    input_keyword = 'id,kw'
    click_enter = 'id,su'

    # keyword = '温一壶清酒 博客园'
    # url = 'https://www.baidu.com'

    def input_key(self, keyword):
        self.send_key(self.input_keyword, keyword)

    def click_search(self):
        self.click(self.click_enter)

    def op_title(self):
        return self.get_title()

    def test_search(self, keyword):
        # self.open(url=self.url)
        log.info("调用搜索：" + keyword)
        self.input_key(keyword)
        self.click_search()
        self.sleep(2)