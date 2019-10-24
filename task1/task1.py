# coding: utf-8

import csv
import requests

url = 'http://127.0.0.1:8000/tasks/api/'
req = requests.get(url)

dict_data = req.json() # 将 json 格式字符串转为字典

print('请求完成：', url)
articles = dict_data.get('articles') # 字典 get 方法

results = []
with open('task1.csv', 'w', encoding='utf-8') as f:  # 打开 task1.csv 并写入
    f_csv = csv.writer(f)  # 将文件对象作为参数传给csv.writer()

    for item in articles:
        line = [item['id'], item['title'], item['image'], item['readcount']]  # 把各项信息组成列表，用于写入 csv
        results.append(line)  # 将结果保存在一个列表
        f_csv.writerow(line)  # 一次写入一行信息

print('保存 csv 完成')
