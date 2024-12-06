# -*- coding: utf-8 -*-

"""
--------------------------------------------
author: 子不语
date: 2024/12/3
contact: 【公众号】思维兵工厂
description: 基于Jina Reader，将html内容转为markdown格式

官网：https://jina.ai/reader/

https://hub.baai.ac.cn/view/39924

--------------------------------------------
"""

import requests
from dataclasses import dataclass


@dataclass
class Markdown:
    title: str
    source: str
    content: str


def convert_url_to_md(url: str):
    """
    请求url获取html内容，转为markdown格式
    :param url:
    :return:
    """

    url = f'https://r.jina.ai/{url}'

    # 在官网中，demo代码需要添加 Authorization 参数；但目前不添加也可以
    # headers = {'Authorization': 'Bearer jina_72481aeb67be4a8da44eec0c6f39f3c6ogXjDzSd3ZhtCRs0yEJ_oC79sslE'}
    # headers = {'Authorization': 'Bearer jina_72481aeb67be4a8da44eec0c6f39f3c6ogXjDzSd3ZhtCRs0yEJ_oC79sslE'}

    response = requests.get(url)

    lines = response.text.split('\n')

    title = ''
    source = ''
    for line in lines:

        if line.startswith('Title:'):
            title = line.replace('Title:', '').strip()

        if line.startswith('URL Source:'):
            source = line.replace('URL Source:', '').strip()

        if title and source:
            break

    content_start_line = lines.index('Markdown Content:') + 1
    content = '\n'.join(lines[content_start_line:])

    return Markdown(title, source, content)


if __name__ == '__main__':
    result = convert_url_to_md('https://hub.baai.ac.cn/view/39924')
    # result = convert_url_to_md('https://blog.csdn.net/gaoxukkk888/article/details/144181862?spm=1001.2100.3001.7377')
    # result = convert_url_to_md('https://chainless.hk/zh-hans/2023/11/26/dw20%e5%8e%bb%e4%b8%ad%e5%bf%83%e6%9c%ac%e4%bd%8d%e5%b8%81%e7%9a%84%e5%ae%9e%e7%8e%b0/')
    # result = convert_url_to_md('https://bbs.kanxue.com/thread-282373.htm')
    # print(result)
    print(result.content)
    print('------------title------------')
    print(result.title)
    print('------------source------------')
    print(result.source)




