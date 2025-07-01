# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f672. FJCU_109_Winter_Day1_Lab1 數字轉二進位


while True:
    try:
        n, m = map(int, input().split())
        n_bin = bin(n)[2:]
        if m <= len(n_bin):
            print(n_bin[-m])
        else:
            print(0)
    except EOFError:
        break
