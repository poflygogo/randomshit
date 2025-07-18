# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e610. 中文網址

import urllib.parse

while True:
    try:
        url = input()
        base_url, query_string = url.split('?', 1)
        decode_query_string = urllib.parse.unquote(query_string, encoding='utf-8')
        print(f'{base_url}?{decode_query_string}')
    except EOFError:
        break
