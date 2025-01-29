# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g796. 檔案分類 (Files)
# 2021-11 TOI 練習賽 新手組


counter = {}
for _ in range(int(input())):
    group = int(input()[3:5])
    counter[group] = counter.get(group, 0) + 1

print('\n'.join(f'{i} {counter[i]}' for i in sorted(counter)))
