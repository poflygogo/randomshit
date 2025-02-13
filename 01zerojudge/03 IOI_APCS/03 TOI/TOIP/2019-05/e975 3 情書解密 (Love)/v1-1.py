# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e975. 3. 情書解密 (Love)
# 2019-05 TOI 練習賽 新手組


text = input()

trans = {i: i + 1 for i in range(65, 91)}
trans.update({i: i + 1 for i in range(97, 123)})
trans[90], trans[122] = 65, 97

k = 0
while 'love' not in text and 'Love' not in text:
    text = text.translate(trans)
    k += 1

print(k)
