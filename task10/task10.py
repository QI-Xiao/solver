# coding: utf-8

import re, datetime
import requests

today = datetime.date.today()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Host': '127.0.0.1:8000',
    'Cookie': 'csrftoken=cGIJZeAcwBL75n7KzskxG9seKynFh9JxAvEJwmpIxiCst5SQwjCTLWTRAEJHtEF1; sessionid=bes62kv3zs80w4sxt2y6tz11ouhuu82h',
}

host = 'http://127.0.0.1:8000'
path_list = '/tasks/tutorial/1/'

req = requests.get(host + path_list, headers=headers)

req_text = req.text

# 以下全是解密的过程，具体过程可参见文本说明
readcount = re.findall("var readcount = '(\S+)';", req_text)[0]
join_str = re.findall("var join_str = '(\S+)';", req_text)[0]
num_list = re.findall("var num_list = '(\S+)';", req_text)[0]

print(readcount, join_str, num_list)

read_list = readcount.split(join_str)
print(read_list)

real_num_list = []
for item in read_list:
    one_num = (int(item) - today.month) // today.day
    # print(one_num)
    real_num_list.append(str(num_list[one_num]))

real_num = ''.join(real_num_list)

print('阅读数', real_num)