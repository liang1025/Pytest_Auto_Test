# encoding=utf-8

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: ExcelList
@time: 2020-07-05 13:26
@desc:
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from common.ExcelData import ExcelData


class ExcelList():
    def get_ids(self):
        ed = ExcelData()
        ids = [
            "测试：{}--->输入值:{}--->断言值:{}--->预期:{}".
                format(data["用例编号"], data["操作输入值"], data["断言"], data["预期值"]) for data in ed.get_excel_datas()
        ]
        return ids