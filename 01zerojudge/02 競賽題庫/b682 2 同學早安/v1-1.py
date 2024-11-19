# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge b682. 2. 同學早安
# 2015高雄市資訊學科能力競賽高中組


h1, m1 = map(int, input().split())
h2, m2 = map(int, input().split())

time = (1440 + h2 * 60 + m2 - h1 * 60 - m1) % 1440
print(time // 60, time % 60)
