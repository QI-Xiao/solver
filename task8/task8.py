# coding: utf-8

import time
import requests

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Host': '127.0.0.1:8000',
    'Cookie': 'csrftoken=cGIJZeAcwBL75n7KzskxG9seKynFh9JxAvEJwmpIxiCst5SQwjCTLWTRAEJHtEF1; sessionid=bes62kv3zs80w4sxt2y6tz11ouhuu82h',
}

new_url = 'http://127.0.0.1:8000/tasks/tutorial/new/'

# 需要先 get 获得一个 csrftoken，然后再 post，否则无法 post
# 所以需要用到：会话对象，会话对象让你能够跨请求保持某些参数
# 可参见：https://requests.kennethreitz.org/zh_CN/latest/user/advanced.html#prepared-request
client = requests.Session()

req = client.get(new_url, headers=headers)

html_text = req.text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

# 找到 csrftoken 的值
csrftoken = soup.find('form').find('input', {'name': 'csrfmiddlewaretoken'}).get('value')

print('csrftoken', csrftoken)

# 把需要 post 的内容生成一个字典
payload = dict(title='测试', content='内容内容内容', index=73, csrfmiddlewaretoken=csrftoken)
print('payload', payload)

time.sleep(3) # 暂停一段时间，不要过快请求

# post 请求，带上提交的内容
r = requests.post(new_url, data=payload, headers=headers)
print(r.text)
