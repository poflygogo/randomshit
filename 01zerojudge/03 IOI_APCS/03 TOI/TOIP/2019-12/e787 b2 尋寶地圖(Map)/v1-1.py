# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e787. b2.尋寶地圖(Map)
# 2019-12 TOI 練習賽


row, col = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(row)]
input() # 幹你娘測資中間有多餘的空白行，這年頭連題目也要唬人
convert = [tuple(map(int, input().split())) for _ in range(row)]

for r in range(row):
    for c in range(col):
        if (sum(convert[r]) + sum(convert[i][c] for i in range(row)) - convert[r][c]) % 2:
            data[r][c] ^= 1

print('\n'.join(' '.join(map(str, r)) for r in data))
