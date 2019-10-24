# coding: utf-8

import requests

url_unchange = 'http://127.0.0.1:8000/static/tasks/djangogirl/' # url 中不变的部分

for i in range(0, 18):
    name = 'content{}.html'.format(i) # 变化的部分拼接出来

    url = url_unchange + name
    req = requests.get(url)
    text = req.content.decode('utf-8') # 将获得的二进制内容用 utf-8 解码

    with open(name, 'w', encoding='utf-8') as f: # 保存成一个新的 HTML 格式文本
        f.write(text)

    print(name, '写入完成')
