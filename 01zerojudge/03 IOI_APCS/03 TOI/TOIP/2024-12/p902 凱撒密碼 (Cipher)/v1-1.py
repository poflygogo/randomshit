# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p902. 凱撒密碼 (Cipher)
# 2024-12 TOI 練習賽 新手組 第三題


text = input()
k = int(input())
print(text.translate({i + j: (i + k) % 26 + j for i in range(26) for j in (65, 97)}))
