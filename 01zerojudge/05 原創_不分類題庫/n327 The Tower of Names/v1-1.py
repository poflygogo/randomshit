# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n327. The Tower of Names


data = [input() for _ in range(int(input()))]
data.sort(key=lambda x: (len(x), x))
print('\n'.join(data))
