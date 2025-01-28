# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g006. 密碼備忘錄 (Password)
# 2021-05 TOI 練習賽 新手組


code = input()
counter = {}
for i in code:
    counter[i] = counter.get(i, 0) + 1
print(''.join(sorted(counter, key=lambda x: (-counter[x], x))))
