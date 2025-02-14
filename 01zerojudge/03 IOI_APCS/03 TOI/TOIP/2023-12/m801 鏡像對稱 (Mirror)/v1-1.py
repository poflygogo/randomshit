# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m801. 鏡像對稱 (Mirror)
# 2023-12 TOI 練習賽 新手組 第二題


text = input()
pattern = 'AHIMOTUVWXY'

flag = True
for i in range(len(text) // 2):
    if text[i] != text[-1 - i] or text[i] not in pattern:
        flag = False
        break
if flag and len(text) & 1 and text[len(text) // 2] not in pattern:
    flag = False
print('Yes' if flag else 'No')
