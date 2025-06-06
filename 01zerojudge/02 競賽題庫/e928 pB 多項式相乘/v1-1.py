# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e928. pB. 多項式相乘
# 2015大學學測推甄申請二階


# dict[冪次, 係數]
input()
expr1 = {i:j for i, j in enumerate(map(int, reversed(input().split())))}
input()
expr2 = {i:j for i, j in enumerate(map(int, reversed(input().split())))}

result_dict = {}
for a1, b1 in expr1.items():
    for a2, b2 in expr2.items():
        a = a1 + a2
        result_dict[a] = result_dict.get(a, 0) + b1 * b2

result_list = [result_dict[i] for i in range(max(result_dict) + 1)]
while result_list[-1] == 0:
    result_list.pop()

print(len(result_list) - 1, ' '.join(map(str, reversed(result_list))), sep='\n')
