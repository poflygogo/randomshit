# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h033. 雜訊移除 (Noise)
# 2021-12 TOI 練習賽 新手組


text, noise = input().split()
text = text.replace(noise, '')
if all(text[i] == text[-1 - i] for i in range(len(text) // 2)):
    print('Yes')
else:
    print('No')
