# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge f515. 英文縮寫 (Abbreviation)
# 2020-12 TOI 練習賽 新手組


table = {'for': '4', 'to': '2','and': 'n', 'you': 'u'}
result = []
for text in input().split():
    if text.lower() in table:
        result.append(table[text.lower()])
    else:
        result.append(text[0].upper())

print(''.join(result))
