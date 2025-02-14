# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m801. 鏡像對稱 (Mirror)
# 2023-12 TOI 練習賽 新手組 第二題


text = input()
pattern = 'AHIMOTUVWXY'

if text == text[::-1] and all(i in pattern for i in text[:len(text) // 2 + 1]):
    print('Yes')
else:
    print('No')
