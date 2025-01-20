# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge f515. 英文縮寫 (Abbreviation)
# 2020-12 TOI 練習賽 新手組


table = {'FOR': '4', 'TO': '2','AND': 'n', 'YOU': 'u'}
result = []
for text in input().split():
    text = text.upper()
    result.append(table.get(text, text[0]))
print(''.join(result))
