# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b458. 非黑即白


color = (0, 255)
t = int(input())
width, height = map(int, input().split())
print(width, height)
for _ in range(height):
    data = list(map(int, input().split()))
    for i in range(0, width * 3, 3):
        k = sum(data[i:i + 3]) / 3
        data[i:i + 3] = [color[k >= t]] * 3
    print(*data)
