# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e787. b2.尋寶地圖(Map)
# 2019-12 TOI 練習賽


row, col = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(row)]
input() # 幹你娘測資中間有多餘的空白行，世風日下，這年頭連題目也要這樣唬人
convert = [list(map(int, input().split())) for _ in range(row)]

convert_row_sum = [sum(r) for r in convert]
convert_col_sum = [sum(convert[r][c] for r in range(row)) for c in range(col)]

for r in range(row):
    for c in range(col):
        if (convert_row_sum[r] + convert_col_sum[c] - convert[r][c]) % 2:
            data[r][c] ^= 1

print('\n'.join(' '.join(map(str, r)) for r in data))
