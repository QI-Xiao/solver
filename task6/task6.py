# coding: utf-8

import csv, re, time
import requests

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Host': '127.0.0.1:8000',
}

host = 'http://127.0.0.1:8000'
path_list = '/tasks/tutorial/list/'

req = requests.get(host + path_list, headers=headers) # 添加 headers，让请求可以通过

soup = BeautifulSoup(req.text, 'lxml')

li_list = soup.find('div', 'panel panel-default').ul.find_all('li')

for li in li_list[0:11]:  # 只抓取前十课 python 教程，后面的需要登录，需要另外处理
    href = li.a['href']
    title = li.span.get_text(strip=True)

    time.sleep(2.1) # 限制访问频率
    req_item = requests.get(host+href, headers=headers) # 进入详细页面再次抓取
    soup_item = BeautifulSoup(req_item.text, 'lxml')

    content = str(soup_item.find('div', 'ppx-main-block'))
    print(content)

    with open(title + '.html', 'w', encoding='utf-8') as f: # 保存成一个新的 HTML 格式文本
        f.write(content)

    print(title, '保存成功')
