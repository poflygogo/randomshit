# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e975. 3. 情書解密 (Love)
# 2019-05 TOI 練習賽 新手組


text = input().lower()

trans = {i: i + 1 for i in range(97, 123)}
trans[122] = 97

k = 0
while 'love' not in text:
    text = text.translate(trans)
    k += 1

print(k)


# 其實這應該要 WA，如果測資包含 loVE 等類似的格式，就會出錯
