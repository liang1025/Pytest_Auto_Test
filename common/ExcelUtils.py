# encoding=utf-8

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: ExcelData
@time: 2020-06-21 15:38
@desc:
'''
import xlrd
from xlrd import xldate_as_tuple
import datetime

# xlrd中单元格的数据类型
# 数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换
# 成我们想要的数据类型
# 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error


class ExcelUtils():
    # 初始化方法
    def __init__(self, data_path, sheet_name):
        self.data_path = data_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        data = xlrd.open_workbook(self.data_path)
        sheet = data.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    def get_row_values(self):
        row_values = self.sheet.row_values(0)
        return row_values

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_values(self, row_index, col_index):
        cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_merged_cell(self):
        merged = self.sheet.merged_cells
        return merged

    def get_merged_cell_value(self, row_index, col_index):
        # 获取合并单元格&单个单元格数据
        cell_value = None
        for(rlow, rhigh, clow, chigh) in self.get_merged_cell():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.__get_cell_values(rlow, clow)
                    break
                else:
                    cell_value = self.__get_cell_values(row_index, col_index)
            else:
                cell_value = self.__get_cell_values(row_index, col_index)
        return cell_value

    def get_cell_value_by_dict(self):
        # 获取数据并转换格式
        # 定义空数组
        all_data_list = []
        # 获取首行数据
        first_row = self.sheet.row_values(0)
        for row in range(1, self.get_row_count()):
            # 定义空列表
            row_dict = {}
            for col in range(self.get_col_count()):
                # col不入参0，输出格式为json数组，增加参数0，则为json对象
                # 获取单元格数据类型
                c_type = self.sheet.cell(row, col).ctype
                # 获取单元格数据
                c_cell = self.get_merged_cell_value(row, col)
                if c_type == 2 and c_cell % 1 == 0:  # 如果是整形
                    c_cell = int(c_cell)
                elif c_type == 3:
                    # 转成datetime对象
                    date = datetime.datetime(*xldate_as_tuple(c_cell, 0))
                    c_cell = date.strftime('%Y/%m/%d %H:%M:%S')
                elif c_type == 4:
                    c_cell = True if c_cell == 1 else False
                # 循环每一个有效的单元格，将字段与值对应存储到字典中
                row_dict[first_row[col]] = c_cell
                # row_dict[self.get_row_values()[col]] = c_cell
            # 再将字典追加到列表中
            all_data_list.append(row_dict)
        # 返回从excel中获取到的数据：以列表存字典的形式返回
        return all_data_list


# if __name__ == '__main__':
#     current_path = os.path.dirname(__file__)
#     excel_path = os.path.join(current_path, '..', 'file/excel/testcase.xlsx')
#     excelUtils = ExcelUtils(excel_path, "Sheet1")
#     print(excel_path)
#     datas =excelUtils.get_cell_value_by_dict()
#     print(datas)