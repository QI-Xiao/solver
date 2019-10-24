# coding: utf-8

import csv, re
import requests

from bs4 import BeautifulSoup

host = 'http://127.0.0.1:8000'
path_list = '/tasks/article/list/'
req = requests.get(host + path_list)

# print(req.text)

soup = BeautifulSoup(req.text, 'lxml')  # 初始化一个 BeautifulSoup 对象

# 寻找所有类为 lab-inner-block 的 a 元素,返回的是一个列表，每一项是一个文章中的数据
data_list = soup.find('div', 'row lab-row').find_all('a', 'lab-inner-block')

results = []
for item in data_list:
    item_href = item['href'] # 详细页的 url 中的路径
    print('开始请求', item_href)

    req_item = requests.get(host + item_href)

    soup_item = BeautifulSoup(req_item.text, 'lxml')  # 再次初始化一个 BeautifulSoup 对象

    title = soup_item.h2.get_text(strip=True)  # 文章标题
    count_list = soup_item.h5.find_all('span')  # 阅读数等数据所在位置

    dict = {'title': title}

    for data in count_list:
        count_data = data.get_text(strip=True).split('：')   # 把阅读数等数据用 ： 分开
        print(count_list)
        dict[count_data[0]] = count_data[1]   # 把阅读数等数据用字典保存，键是阅读数，值是具体数值

    print('获得数据：', dict)

    results.append(dict) # 把一篇文章的所有数据作为一个列表的一项

print(results)