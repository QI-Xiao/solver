# coding: utf-8

import requests

host = 'http://127.0.0.1:8000' # host 名
api_path = '/tasks/api/' # 路径
req = requests.get(host + api_path)

dict_data = req.json()

print('请求完成')

articles = dict_data.get('articles')

for item in articles:
    image_path = item['image'] # 图片路径
    image_name = image_path.split('/')[-1] # 图片名
    print('图片地址：', image_path, '图片名：', image_name)

    req_img = requests.get(host + image_path)

    with open(image_name, 'wb') as f: # 二进制格式写入
        f.write(req_img.content)

    print(image_name, '保存成功')

print('保存图片完成')
