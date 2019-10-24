# coding: utf-8

import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Host': '127.0.0.1:8000',
    'Cookie': 'csrftoken=cGIJZeAcwBL75n7KzskxG9seKynFh9JxAvEJwmpIxiCst5SQwjCTLWTRAEJHtEF1; sessionid=bes62kv3zs80w4sxt2y6tz11ouhuu82h',
}

host = 'http://127.0.0.1:8000'
path_list = '/tasks/tutorial/1/'

req = requests.get(host + path_list, headers=headers)

req_text = req.text

# 用正则表达式分别找到 点赞数 和 评论数 编码后的数据
likecount = re.findall('<span class="num">点赞数：(\S+)</span>', req_text)[0]
commentcount = re.findall('<span class="num">评论数：(\S+)</span>', req_text)[0]
# print(req.text)

print(likecount, commentcount)

# 找到对应的编码规则
ENCODE_LIST = {
    '&#xF369;': '0',
    '&#xF52C;': '1',
    '&#xe072;': '2',
    '&#xF2bd;': '3',
    '&#xF51D;': '4',
    '&#xF7D9;': '5',
    '&#xE52C;': '6',
    '&#xF783;': '7',
    '&#xE8B8;': '8',
    '&#xEB7F;': '9',
}

like_list = likecount.split(';')
comment_list = commentcount.split(';')
print(like_list, comment_list, like_list[:-1])

like_num = ''.join(ENCODE_LIST[i+';'] for i in like_list[:-1]) # 根据对应的编码换算到数字
comment_num = ''.join(ENCODE_LIST[i+';'] for i in comment_list[:-1])

print('点赞数:', like_num, '  评论数:', comment_num)
