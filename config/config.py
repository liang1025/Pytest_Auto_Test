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

    # 保存driver
    _global_dict['driver'] = None


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