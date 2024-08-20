"""
第一行各數字分別代表h,w,r1,c1,r2,c2
共6個數字
h = 高度, w = 寬度
(r1, c1) = 開始的字母座標
(r2, c2) = 結束的字母座標
"""

from sys import stdin

# 初步整理資料
data = stdin.readlines()
info = tuple(map(int, data.pop(0).split()))

# 取向量, 並將其歸1或0
arrow = (info[4]-info[2], info[5]-info[3])
arrow = tuple(map(lambda x: 1 if x > 0 else 0 , arrow))

result = ''
coordinate = [info[2], info[3]]
while (coordinate[0] <= info[4]) and (coordinate[1] <= info[5]):
    result += data[coordinate[0]-1][coordinate[1]-1]
    coordinate[0] += arrow[0]
    coordinate[1] += arrow[1]

print(result)