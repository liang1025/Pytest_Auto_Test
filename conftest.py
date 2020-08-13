'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: conftest.py
@time: 2020-05-23 21:49
@desc:
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
from selenium import webdriver
import config.config as cf
from common.mainModule import log
from py._xmlgen import html
import time


@pytest.fixture(scope='function')
def quit_driver():
    # log.info("conftest文件初始化")
    # cf.init()
    binary_location = '/usr/bin/google-chrome'
    chrome_driver_binary = '/usr/bin/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = binary_location
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')  # 窗口最大化
    # 新版google不显示正在受自动化软件控制
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # driver = webdriver.Chrome(options=chrome_options)
    os.environ["webdriver.chrome.driver"] = chrome_driver_binary
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
    driver.get(cf.get_value('site'))
    log.info('打开的网址是：' + cf.get_value('site'))
    log.info("初始化driver")
    cf.set_value('driver', driver)
    yield
    driver.quit()
    log.info('关闭浏览器')


@pytest.fixture(scope='module')
def clear_report():
    log.info('运行代码')
    # cf.init() # 以pytest框架方式运行代码需要开启
    log.info('全局初始化')
    yield
    # time.sleep(5)
    # log.info("报告延迟处理10s")
    init_report = 'allure generate --clean ./report'
    os.system(init_report)
    log.info("测试报告json文件初始化成功！")
    time.sleep(2)
    report_path = 'del /f /q G:\\202001-202012\\pytest\\Pytest_Auto_Test\\report'
    log.info(report_path)
    os.system(report_path)
    log.info("删除report下的json文件")


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    解决乱码问题
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """当测试失败的时候，自动截图，展示到html报告中"""
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:250px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         report.description = str(item.function.__doc__)
#         report.module = str(item.module.__doc__)
#         # report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码
#
#
# def _capture_screenshot():
#     '''截图保存为base64'''
#     return cf.get_value('driver').get_screenshot_as_base64()


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    '''优化测试报告标题'''
    report.title = "搜索测试报告（基于Pytest）"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    '''添加测试人员信息'''
    prefix.extend([html.p("测试人员：温一壶清酒")])
    prefix.extend([html.p("测试部门：自动化测试中心")])


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    '''插入列信息'''
    cells.insert(2, html.th('模块'))
    cells.insert(3, html.th('描述'))
    cells.insert(4, html.th('时间', class_='sortable time', col='time'))
    cells.pop()


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    '''添加列信息的值'''
    cells.insert(2, html.td(report.module))
    cells.insert(3, html.td(report.description))
    report_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    cells.insert(4, html.td(report_time, class_='col-time'))
    cells.pop()


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "搜索测试项目demo"
    config._metadata['接口地址'] = 'https://www.cnblogs.com/hong-fithing/'
    # 删除Java_Home
    # config._metadata.pop("JAVA_HOME")