# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q881. 快樂學幾何2


from sys import stdin

data = stdin.read().splitlines()
print('\n'.join(str(pow(int(i.split()[1]), 2) // 2) for i in data))
