# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e797. p4. 數位邏輯運算
# 2019-12 TOI 新手同好會


N, T = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(N)]
result_and = []
result_or = []
result_xor = []
for i in range(T):
    a = b = c = data[0][i]
    for j in range(1, N):
        a &= data[j][i]
        b |= data[j][i]
        c ^= data[j][i]
    result_and.append(a)
    result_or.append(b)
    result_xor.append(c)

print(f'AND: {" ".join(map(str, result_and))}')
print(f' OR: {" ".join(map(str, result_or))}')
print(f'XOR: {" ".join(map(str, result_xor))}')
