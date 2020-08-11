# encoding=utf-8

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: Argprase
@time: 2020-08-09 16:27
@desc:
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import config.config as cf
import argparse
from common.mainModule import log


class Argprase():

    def get_args(self):
        cf.init()
        """命令行参数解析"""
        parser = argparse.ArgumentParser(description=u'可选择参数：')
        parser.add_argument('-e', '--environment', choices=['test', 'prod'], default='test',
                            help=u'测试环境test，线上环境prod')
        parser.add_argument('-m', '--mark', choices=['mock', 'jenkins'], default='mock',
                            help=u'测试环境百度mock，线上环境jenkins登录')
        args = parser.parse_args()
        args_env = args.environment
        log.info('args数据：' + str(args_env))
        log.info('args数据：' + str(args))
        if args.environment in ('test', 'test'):
            cf.set_value('environment', 'test')
            cf.set_value('site', 'http://www.baidu.com/')
        elif args.environment in ('prod', 'prod'):
            cf.set_value('environment', 'prod')
            cf.set_value('site', 'a')
        else:
            exit()
            print("请输入test/prod")
        if args.mark in ('jen', 'jenkins'):
            cf.set_value('mark', 'jenkins')
        elif args.mark in ('mo', 'mock'):
            cf.set_value('mark', 'mock')
        else:
            exit()
            print("请输入jenkins/mock")
        log.info('获取到的site地址：' + cf.get_value('site'))