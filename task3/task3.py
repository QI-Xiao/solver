# coding: utf-8

import csv
import requests

from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/tasks/article/list/'
req = requests.get(url)

# print(req.text)

soup = BeautifulSoup(req.text, 'lxml')  # 初始化一个 BeautifulSoup 对象

# 寻找所有类为 lab-inner-block 的 a 元素,返回的是一个列表，每一项是一个文章中的数据
data_list = soup.find('div', 'row lab-row').find_all('a', 'lab-inner-block')

results = []
for i in data_list:
    h3 = i.h3.get_text(strip=True) # 标题
    p = i.p.get_text(strip=True) # 摘要
    results.append([h3, p])

print('请求数据：', results)

with open('task3.csv', 'w', encoding='utf-8') as f:  # 打开 task3.csv 并写入
    f_csv = csv.writer(f)  # 将文件对象作为参数传给csv.writer()
    f_csv.writerows(results) # 一次写入所有信息

print('保存 csv 完成')
