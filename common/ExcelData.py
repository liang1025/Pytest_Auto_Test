# encoding=utf-8

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: ExcelData
@time: 2020-07-05 13:52
@desc:
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import os
import common.ExcelUtils as excel


class ExcelData():
    def get_excel_datas(self):
        current = os.getcwd()
        data_path = current + "/file/excel/testcase.xlsx"
        sheetname = "Sheet1"
        get_data = excel.ExcelUtils(data_path, sheetname)
        datas = get_data.get_cell_value_by_dict()
        return datas