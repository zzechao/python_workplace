# -*- coding: UTF-8 -*-

import os
from os.path import join, getsize
import json
import xlwt

so_432_path = '/Users/zhouzechao/Desktop/python_workplace/yyxunhuan-4.32.0-SNAPSHOT-7014-official/lib/armeabi-v7a'
so_425_path = '/Users/zhouzechao/Desktop/python_workplace/yyxunhuan-4.25.10-5562-official/lib/armeabi-v7a'
json_so_path = '/Users/zhouzechao/Desktop/python_workplace/so.json'


def requestUrlAndWriteToExcel(a, b):
    # writ
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook('utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet(b)

    line = 0
    worksheet.write(line, 0, 'so名')
    worksheet.write(line, 1, '包名')
    worksheet.write(line, 2, '负责人')
    worksheet.write(line, 3, '大小')

    with open(json_so_path, 'r') as f:
        sos = json.loads(f.read())

        dirs = os.listdir(a)
        # 输出所有文件和文件夹
        for file in dirs:
            line = line + 1
            worksheet.write(line, 0, file)
            print(file)
            stat = False
            for so in sos:
                if file == so['lib']:
                    stat = True
                    worksheet.write(line, 1, str(
                        so['group_id'] + ':' + so['artifact_id']))
                    worksheet.write(line, 2, so['admin'])
                    kb = int(getsize(join(a, file)) / 1024)
                    worksheet.write(line, 3, kb)
                    print(so['lib'] + '---' + so['group_id'] + '---' +
                          str(int(getsize(join(a, file)) / 1024)) + 'KB')
                    break
            if not stat:
                kb = float(getsize(join(a, file)) / 1024)
                worksheet.write(line, 3, kb)

    # 保存
    workbook.save('so_info_excel' + b + '.xls')
    print('workbook save success')


if __name__ == "__main__":
    # requestUrlAndWriteToExcel(so_430_path, '4.30.3的so依赖信息')
    requestUrlAndWriteToExcel(so_432_path, '4.32.0的so依赖信息')
