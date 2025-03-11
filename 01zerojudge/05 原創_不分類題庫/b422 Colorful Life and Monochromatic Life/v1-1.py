# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b422. Colorful Life and Monochromatic Life


width, height = map(int, input().split())
print(width, height)
for _ in range(height):
    data = list(map(int, input().split()))
    for i in range(0, width * 3, 3):
        t = round(sum(data[i:i + 3]) / 3)
        data[i:i + 3] = [t] * 3
    print(*data)
