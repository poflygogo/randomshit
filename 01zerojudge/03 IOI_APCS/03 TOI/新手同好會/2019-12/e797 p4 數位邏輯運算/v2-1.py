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
    result_and.append(1 if all(data[j][i] == 1 for j in range(N)) else 0)
    result_or.append(1 if any(data[j][i] == 1 for j in range(N)) else 0)
    result_xor.append(1 if sum(data[j][i] for j in range(N)) % 2 != 0 else 0)

print(f'AND: {" ".join(map(str, result_and))}')
print(f' OR: {" ".join(map(str, result_or))}')
print(f'XOR: {" ".join(map(str, result_xor))}')
