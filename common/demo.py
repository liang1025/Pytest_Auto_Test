'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: demo
@time: 2020-07-23 21:40
@desc:
'''

import xlrd
import os
import datetime
from xlrd import xldate_as_tuple

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '..', 'file/excel/testcase.xlsx')
excel_object = xlrd.open_workbook(excel_path)
sheet_object = excel_object.sheet_by_name('Sheet1')
# # 获取第一行数据
# rows_cell_value = sheet_object.row_values(0)
# print('获取到的第一行数据为：' + str(rows_cell_value))
# # 获取第一行、第一列单元格数据
# row_cell_value1 = sheet_object.cell_value(0, 0)
# print('获取坐标为第一行、第一列单元格的数据为：' + row_cell_value1)
# # 获取第二行、第四列单元格数据
# row_cell_value2 = sheet_object.cell_value(1, 3)
# print('获取坐标为第二行、第四列单元格的数据为：' + row_cell_value2)
# # 获取第四列数据
# cols_cell_value = sheet_object.col_values(3)
# print('获取第四列的数据为：' + str(cols_cell_value))
# # 获取单元格类型
# # 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
# cell_value_type1 = sheet_object.cell_type(2, 0)
# print('单元格类型为：' + str(cell_value_type1))
# cell_value_type2 = sheet_object.cell_type(1, 0)
# print('单元格类型为：' + str(cell_value_type2))
# cell_value_type3 = sheet_object.cell_type(1, 7)
# print('单元格类型为：' + str(cell_value_type3))
# cell_value_type4 = sheet_object.cell_type(1, 8)
# print('单元格类型为：' + str(cell_value_type4))
# cell_value_type5 = sheet_object.cell_type(2, 8)
# print('单元格类型为：' + str(cell_value_type5))
# # 获取有效行数
# row_nrows = sheet_object.nrows
# print('当前sheet页中有效行数为：' + str(row_nrows))
# # 获取有效列数
# col_ncols = sheet_object.ncols
# print('当前sheet页中有效列数为：' + str(col_ncols))
# # 获取当前行的单元格长度
# row_length = sheet_object.row_len(0)
# print('第一行的有效单元格长度为：' + str(row_length))
# # 获取所有工作表名称
# print('当前excel中的工作表名称为：'+ str(excel_object.sheet_names()))

# 获取有效行数
# row_index = sheet_object.nrows
# # 获取有效列数
# col_index = sheet_object.ncols
# # 定义空数组
# all_data_list = []
# # 获取首行数据
# first_row = sheet_object.row_values(0)
# for row in range(1, row_index):
#     # 定义空列表
#     row_dict = {}
#     for col in range(col_index):
#         c_cell = sheet_object.cell_value(row, col)
#         # 获取单元格数据类型
#         c_type = sheet_object.cell(row, col).ctype
#         if c_type == 2 and c_cell % 1 == 0:  # 如果是整形
#             c_cell = int(c_cell)
#         elif c_type == 3:
#             # 转成datetime对象
#             date = datetime.datetime(*xldate_as_tuple(c_cell, 0))
#             c_cell = date.strftime('%Y-%m-%d')
#         elif c_type == 4:
#             c_cell = True if c_cell == 1 else False
#         # 循环每一个有效的单元格，将字段与值对应存储到字典中
#         row_dict[first_row[col]] = c_cell
#     # 再将字典追加到列表中
#     all_data_list.append(row_dict)
#     print(str(row_dict))

meger_cell = sheet_object.merged_cells
print(str(meger_cell))


def get_meger_cell_value(row_index, col_index):
    cell_value = None
    for(rlow, rhight, clow, chight) in meger_cell:
        if(row_index >= rlow and row_index < rhight):
            if(col_index >= clow and col_index < chight):
                cell_value = sheet_object.cell_value(rlow, clow)
                break
            else:
                cell_value = sheet_object.cell_value(row_index, col_index)
        else:
            cell_value = sheet_object.cell_value(row_index, col_index)
    return cell_value


print(get_meger_cell_value(0, 0))
