# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge b514
# 103學年度商業類程式設計競賽模擬題


for _ in range(int(input())):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())

    y = (a3 * b1 - a1 * b3) // (a2 * b1 - a1 * b2)
    x = (b2 * a3 - a2 * b3) // (a1 * b2 - a2 * b1)
    print(x, y)
