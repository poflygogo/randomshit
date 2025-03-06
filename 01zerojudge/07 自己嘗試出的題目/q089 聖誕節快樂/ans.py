# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q089. 聖誕節快樂


n = int(input())

for i in range(1, n + 1):
    blank = ' ' * (n - i)
    leaf = ' '.join('*' * i)
    print(blank + leaf)

trunk = ' ' * (n - 2) + '| |'
for i in range(n // 2):
    print(trunk)

print('\\' + '_' * (n + (n - 1) - 2) + '/')
