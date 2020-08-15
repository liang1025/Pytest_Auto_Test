# encoding=utf-8

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: mainModule
@time: 2020-05-03 12:34
@desc:
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import logging
import os.path
import time


class Logger:
    def __init__(self, name=__name__):
        self.__name = name
        self.logger = logging.getLogger(self.__name)
        self.logger.setLevel(logging.INFO)

        # 创建一个handler,用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_path = os.getcwd() + '/logs/'  # 本地运行logs地址
        log_path = '/var/jenkins_home/workspace/github_demo/logs'  # 服务器运行logs地址
        # print(log_path)
        # file_hanlder = logging.FileHandler(filename='example.log', encoding='utf-8')
        log_name = log_path + rq + '.log'

        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        handler = logging.FileHandler(log_name, encoding='utf-8')
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(handler)
        self.logger.addHandler(console)

    @property
    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger


log = Logger(__name__).get_log
# log.error('模块直接执行打印日志')
