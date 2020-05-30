'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: conftest.py
@time: 2020-05-23 21:49
@desc:
'''

import pytest
from selenium import webdriver
import config.config as cf
from common.mainModule import log
import os


@pytest.fixture(scope='function')
def quit_driver():
    # cf.init()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')  # 窗口最大化
    # 新版google不显示正在受自动化软件控制
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(cf.get_value('url'))
    log.info('打开的网址是：' + cf.get_value('url'))
    log.info("初始化driver")
    cf.set_value('driver', driver)
    yield
    driver.quit()
    log.info('关闭浏览器')