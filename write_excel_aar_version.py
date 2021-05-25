# -*- coding: UTF-8 -*-
from urllib.error import HTTPError

import requests
import json
import xlwt
from urllib import request
from bs4 import BeautifulSoup

build_id = 54917

# 100625appid
request_url = "https://ci-sdm.yy.com/api/project/build/" + \
              str(build_id) + "/dependencies?page=1&page_size=200&sdk_module_name=&sdk_is_internal=2&sdk_is_compatible=all"

maven_url = "https://repo.yy.com:8181/nexus/content/groups/public/"


def requestUrlAndWriteToExcel():
    res = requests.get(request_url)

    # with request.urlopen("http://repo.yy.com:8181/nexus/content/groups/public/com/duowan/android/DeviceIdentifier
    # /deviceidentifier/100.0.12/") as response: data1 = response.read().decode('utf-8') # 默认即为 utf-8 print(data1)

    # soup = BeautifulSoup(data1,"html.parser")
    # for tag in soup.find_all('tr'):
    #     v = tag.find_all('td')
    #     if len(v) == 4:
    #         if v[0].get_text().endswith('aar'):
    #             size = v[2].get_text().strip()
    #             print(v[0].get_text()+'--'+str(int(int(size)/1024))+'M')

    # print(res.text)
    datas = json.loads(res.text)
    if datas['code'] != 0:
        print("求失败，请稍后再试")
        return

    # writ
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook('utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')

    line = 0
    worksheet.write(line, 0, '名字')
    worksheet.write(line, 1, '包名')
    worksheet.write(line, 2, '版本')
    worksheet.write(line, 3, 'aar')
    worksheet.write(line, 4, 'url')
    worksheet.write(line, 5, '大小')
    line = line + 1
    for data in datas['data']:
        # f.write(data['sdk_name'] + " " + data['module_name'] + " " + data['version'] + "\n")
        print("sdk_name: %s, module_name: %s, version: %s" %
              (data['sdk_name'], data['module_name'], data['version']))
        # 写入excel
        # 参数对应 行, 列, 值
        worksheet.write(line, 0, data['sdk_name'])
        worksheet.write(line, 1, data['module_name'])
        worksheet.write(line, 2, data['version'])
        maven_module = data['module_name'].replace(
            '.', '/').replace(':', '/') + '/'

        module_url = maven_url + maven_module + data['version'] + '/'

        print(module_url)

        if module_url.find('makefriends') == -1 and module_url.find('expblur') == -1:
            try:
                with request.urlopen(module_url) as response:
                    data1 = response.read().decode('utf-8')  # 默认即为 utf-8

                soup = BeautifulSoup(data1, "html.parser")
                for tag in soup.find_all('tr'):
                    v = tag.find_all('td')
                    if len(v) == 4:
                        if v[0].get_text().endswith('aar'):
                            size = v[2].get_text().strip()
                            print(v[0].get_text() + '--' +
                                  str(int(int(size) / 1024)) + 'K')
                            worksheet.write(line, 3, v[0].get_text())
                            worksheet.write(line, 4, module_url)
                            kb = int(int(size) / 1024)
                            if kb > 1024:
                                worksheet.write(
                                    line, 5, str(int(kb / 1024)) + 'MB')
                            else:
                                worksheet.write(line, 5, str(kb) + 'KB')

                pass
            except HTTPError:
                pass

        line = line + 1
    # 保存
    workbook.save('dependencies_excel_' + str(build_id) + '.xls')
    print('workbook save success')


if __name__ == "__main__":
    requestUrlAndWriteToExcel()
