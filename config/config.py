# encoding=utf-8

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: config
@time: 2020-05-03 12:33
@desc:
'''
import os


def init():
    global _global_dict
    _global_dict = {}

    # 代码根目录
    root_dir = os.getcwd()

    # 存放程序所在目录
    _global_dict['root_path'] = root_dir

    # 截图保存路径
    _global_dict['screenshot_path'] = "{}\\file\\screenshot\\".format(root_dir)

    # 保存driver
    _global_dict['driver'] = None

    # url
    _global_dict['url'] = 'https://www.baidu.com'

    # 设置运行环境
    _global_dict['site'] = 'https://www.baidu.com/'
    # 运行环境，默认test，可设为prod
    _global_dict['environment'] = 'test'
    # 标记
    _global_dict['mark'] = 'mock'
    # allure-results
    _global_dict['github_results'] = '/var/jenkins_home/workspace/github_demo/target/allure-results'
    # allure
    _global_dict['allure'] = '/var/jenkins_home/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/allure/bin/allure'



def set_value(name, value):
    """
    修改全局变量的值
    :param name: 变量名
    :param value: 变量值
    """
    _global_dict[name] = value


def get_value(name, def_val='no_value'):
    """
    获取全局变量的值
    :param name: 变量名
    :param def_val: 默认变量值
    :return: 变量存在时返回其值，否则返回'no_value'
    """
    try:
        return _global_dict[name]
    except KeyError:
        return def_val


if __name__ == '__main__':
    init()