# encoding=utf-8

'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: ReportZip
@time: 2020-07-29 21:41
@desc:
'''
import os
import zipfile
from common.mainModule import log


class ReportZip():
    def __init__(self, dir_path, zip_path):
        self.dir_path = dir_path
        self.zip_path = zip_path

    def report_zip(self):
        '''
            :param dir_path: 目标文件夹路径
            :param zip_path: 压缩后的文件夹路径
            :return:
            '''
        log.info("执行打包程序")
        zip = zipfile.ZipFile(self.zip_path, "w", zipfile.ZIP_DEFLATED)
        for(root, dirnames, filenames) in os.walk(self.dir_path):
            file_path = root.replace(self.dir_path, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
            # 循环出一个个文件名
            for filename in filenames:
                zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
        log.info("压缩成功")
        zip.close()
        return zip