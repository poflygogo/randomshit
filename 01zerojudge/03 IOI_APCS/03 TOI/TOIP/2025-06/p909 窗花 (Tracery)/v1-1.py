# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p909. 窗花 (Tracery)
# TOI練習賽202506新手組第1題


w, h = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]
for i in data:
    i.extend(list(reversed(i)))
for i in range(h - 1, -1, -1):
    data.append(data[i])
print('\n'.join(' '.join(map(str, i)) for i in data))
