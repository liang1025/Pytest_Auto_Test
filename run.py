'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: run.py
@time: 2020-05-02 21:05
@desc:
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('温一壶清酒 博客园')
driver.find_element_by_id('su').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
time.sleep(3)
driver.quit()