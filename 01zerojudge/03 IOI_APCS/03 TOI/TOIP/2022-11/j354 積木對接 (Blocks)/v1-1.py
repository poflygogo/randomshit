# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j354. 積木對接 (Blocks)
# 2022-11 TOI 練習賽 新手組


brick_base_n = int(input())
brick_base_rough = map(int, input().split())
brick_insert_n = int(input())
brick_insert_rough = map(int, input().split())

brick_base_info = []
for i, j in enumerate(brick_base_rough):
    if i & 1 == 0:
        brick_base_info.extend([1] * j)
    else:
        brick_base_info.extend([2] * j)

brick_insert_info = []
for i, j in enumerate(brick_insert_rough):
    if i & 1 == 0:
        brick_insert_info.extend([2] * j)
    else:
        brick_insert_info.extend([1] * j)

if any(
    all(j + k <= 3 for j, k in zip(brick_base_info[i:], brick_insert_info))
    for i in range(len(brick_base_info) - len(brick_insert_info) + 1)
    ):
    print('YES')
else:
    print('NO')
