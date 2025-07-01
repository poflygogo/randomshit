# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f672. FJCU_109_Winter_Day1_Lab1 數字轉二進位


while True:
    try:
        n, m = map(int, input().split())
        b = 1 << (m - 1)
        print(1 if n & b else 0)
    except EOFError:
        break
