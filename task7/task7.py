# coding: utf-8
# 与 task6 代码基本一致，只是由于需要登录后访问，所以 headers 加了登录后获得的 cookie

import csv, re, time
import requests

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Host': '127.0.0.1:8000',
    'Cookie': 'csrftoken=cGIJZeAcwBL75n7KzskxG9seKynFh9JxAvEJwmpIxiCst5SQwjCTLWTRAEJHtEF1; sessionid=bes62kv3zs80w4sxt2y6tz11ouhuu82h',
}

host = 'http://127.0.0.1:8000'
path_list = '/tasks/tutorial/list/'

# 与 task6 代码基本一致，只是由于需要登录后访问，所以 headers 加了登录后获得的 cookie
req = requests.get(host + path_list, headers=headers)

soup = BeautifulSoup(req.text, 'lxml')

li_list = soup.find('div', 'panel panel-default').ul.find_all('li')

for li in li_list[11:21]: # 这回抓取 10 -20 课的 python 教程
    href = li.a['href']
    title = li.span.get_text(strip=True)

    time.sleep(2.1)
    req_item = requests.get(host+href, headers=headers)
    soup_item = BeautifulSoup(req_item.text, 'lxml')

    content = str(soup_item.find('div', 'ppx-main-block'))
    print(content)

    with open(title + '.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(title, '保存成功')
