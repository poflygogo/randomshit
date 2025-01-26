# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e806. 1.多項式計算 (Polynomial)
# 2019-11 TOI 練習賽 新手組


n1 = int(input())
expr1 = list(map(int, input().split()))
expr1_dict = {expr1[i]: expr1[i + 1] for i in range(0, n1 * 2, 2)}

n2 = int(input())
expr2 = list(map(int, input().split()))
expr2_dict = {expr2[i]: expr2[i + 1] for i in range(0, n2 * 2, 2)}

for i in expr2_dict:
    expr1_dict[i] = expr1_dict.get(i, 0) + expr2_dict[i]
    if expr1_dict[i] == 0:
        expr1_dict.pop(i)

if not expr1_dict:
    print('NULL!')
else:
    print('\n'.join(f'{i}:{expr1_dict[i]}' for i in sorted(expr1_dict, reverse=True)))
