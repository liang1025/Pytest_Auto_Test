'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: BasePage
@time: 2020-05-03 12:30
@desc:
'''

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import inspect
import time


class BasePage(object):

    def split_locator(self, locator):
        """
        分解定位表达式，如'css,.username',拆分后返回'css selector'和定位表达式'.username'(class为username的元素)
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        :return: locator_dict[by], value:返回定位方式和定位表达式
        """
        by = locator.split(',')[0]
        value = locator.split(',')[1]
        locator_dict = {
            # 'id': 'find_element_by_id',
            # 'name': 'find_element_by_name',
            # 'class_name': 'find_element_by_class_name',
            # 'tag_name': 'find_element_by_tag_name',
            # 'link_text': 'find_element_by_link_text',
            # 'partial_link_text': 'find_element_by_partial_link_text',
            # 'xpath': 'find_element_by_xpath',
            # 'css_selector': 'find_element_by_css_selector',
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            raise NameError("wrong locator!'id','name','class','tag','link','plink','xpath','css',exp:'id,username'")
        return locator_dict[by], value

    def wait_element(self, locator, sec=30 ):
        """
        等待元素出现
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param sec:等待秒数
        """
        by, value = self.split_locator(locator)
        try:
            WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value),
                                                     message='element not found!!!')
            return True
        except TimeoutException:
            return False
        except Exception as e:
            raise e

    def open(self, url):
        """
        打开网址
        :param url: 网址连接
        """
        self.driver.get(url)

    def get_element(self, locator, sec=60):
        """
        获取一个元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param sec:等待秒数
        :return: 元素可找到返回element对象，否则返回False
        """
        if self.wait_element(locator, sec):
            by, value = self.split_locator(locator)
            print(by, value)
            try:
                element = self.driver.find_element(by=by, value=value)
                return element
            except Exception as e:
                raise e
        else:
            return False

    def get_elements(self, locator):
        """
        获取一组元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: elements
        """
        by, value = self.split_locator(locator)
        try:
            elements = WebDriverWait(self.driver, 60, 1).until(lambda x: x.find_elements(by=by, value=value))
            return elements
        except Exception as e:
            raise e

    def clear(self, locator):
        """
        清除元素中的内容
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        self.get_element(locator).clear()

    def send_key(self, locator, text):
        """
        在元素中输入内容
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param text: 输入的内容
        """
        self.get_element(locator).send_keys(text)

    def type(self, locator, text):
        """
        在元素中输入内容
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param text: 输入的内容
        """
        self.get_element(locator).send_keys(text)

    def enter(self, locator):
        """
        在元素上按回车键
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        self.get_element(locator).send_keys(Keys.ENTER)

    def right_click(self, locator):
        """
        鼠标右击元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.get_element(locator)
        ActionChains(self.driver).context_click(element).perform()

    def double_click(self, locator):
        """
        双击元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.get_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    def move_to_element(self, locator):
        """
        鼠标指向元素
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        element = self.get_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def drag_and_drop(self, locator, target_locator):
        """
        拖动一个元素到另一个元素位置
        :param locator: 要拖动元素的定位
        :param target_locator: 目标位置元素的定位
        """
        element = self.get_element(locator)
        target_element = self.get_element(target_locator)
        ActionChains(self.driver).drag_and_drop(element, target_element).perform()

    def drag_and_drop_by_offset(self, locator, xoffset, yoffset):
        """
        拖动一个元素向右下移动x,y个偏移量
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param xoffset: X offset to move to
        :param yoffset: Y offset to move to
        """
        element = self.get_element(locator)
        ActionChains(self.driver).drag_and_drop_by_offset(element, xoffset, yoffset).perform()

    def click(self, locator):
        """
        在元素上单击
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        """
        self.get_element(locator).click()

    def get_title(self):
        """获取title"""
        title = self.driver.title
        return title

    def click_link(self, text):
        """
        按部分链接文字查找并点击链接
        :param text: 链接的部分文字
        """
        self.get_element('plink,' + text).click()

    def alert_text(self):
        """
        返回alert文本
        :return: alert文本
        """
        return self.driver.switch_to.alert.text

    def alert_accept(self):
        """
        alert点确认
        """
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        """
        alert点取消
        """
        self.driver.switch_to.alert.dismiss()

    def get_attribute(self, locator, attribute):
        """
        返回元素某属性的值
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :param attribute: 属性名称
        :return: 属性值
        """
        value = self.get_element(locator).get_attribute(attribute)
        return value

    def get_ele_text(self, locator):
        """
        返回元素的文本
        :param locator: 定位方法+定位表达式组合字符串，用逗号分隔，如'css,.username'
        :return: 元素的文本
        """
        return self.get_element(locator).text

    def js(self, script):
        """
        执行JavaScript
        :param script:js语句
        """
        self.driver.execute_script(script)

    def scroll_element(self, locator):
        """
        拖动滚动条至目标元素
        :param locator: 定位方法+定位表达式组合字符串，如'css,.username'
        """
        script = "return arguments[0].scrollIntoView();"
        element = self.get_element(locator)
        self.driver.execute_script(script, element)

    def scroll_top(self):
        """
        滚动至顶部
        """
        self.js("window.scrollTo(document.body.scrollHeight,0)")

    def scroll_bottom(self):
        """
        滚动至底部
        """
        self.js("window.scrollTo(0,document.body.scrollHeight)")

    def is_text_on_page(self, text):
        """
        返回页面源代码
        :return: 页面源代码
        """
        if text in self.driver.page_source:
            return True
        else:
            return False

    def screenshot(self, info='-'):
        """
        截图,起名为：文件名-方法名-注释
        :param info: 截图说明
        """
        catalog_name = './picture'
        if not os.path.exists(catalog_name):
            os.makedirs(catalog_name)
        class_object = inspect.getmembers(inspect.stack()[1][0])[-3][1]['self']  # 获得测试类的object
        classname = str(class_object).split('.')[1].split(' ')[0]  # 获得测试类名称
        testcase_name = inspect.stack()[1][3]  # 获得测试方法名称
        filepath = catalog_name + classname + "@" + testcase_name + info + ".png"
        self.driver.get_screenshot_as_file(filepath)

    def switch_menue(self, parentelement, secelement, targetelement):
        """三级菜单切换"""
        self.sleep(3)
        # noinspection PyBroadException
        try:
            self.driver.switch_to_default_content()
            self.click(parentelement)
            self.click(secelement)
            self.click(targetelement)
        except BaseException:
            print('切换菜单报错')

    def switch_ifarme(self, selector):
        """切换ifarme"""
        element = self.get_element(selector)
        # noinspection PyBroadException
        try:
            self.driver.switch_to.frame(element)
        except BaseException:
            print('切换菜单报错')

    def quit_iframe(self):
        """退出当前iframe"""
        self.driver.switch_to_default_content()

    def close(self):
        """
        关闭当前页
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def quit(self):
        """
        关闭页面
        """
        self.driver.quit()

    def sleep(self, sec):
        time.sleep(sec)