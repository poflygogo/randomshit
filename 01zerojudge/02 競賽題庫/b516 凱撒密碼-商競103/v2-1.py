# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b516. 凱撒密碼-商競103


A = ord('A')

for i in range(int(input())):
    text = input().strip()
    print(''.join(chr((ord(i) - A + 3) % 26 + A) for i in text))
