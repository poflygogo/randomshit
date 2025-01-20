# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge f514. 拼字遊戲 (Spelling)
# 2020-12 TOI 練習賽 新手組


alpha = list(input())
target = input()

result = []
for item in target:
    try:
        idx = alpha.index(item)
    except ValueError:
        idx = None
    else:
        alpha[idx] = None
    finally:
        result.append(str(idx + 1) if idx is not None else 'X')

print(*result)
