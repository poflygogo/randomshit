# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h495. 農家樂(Agricola)


table = [-1, 1, 1, 2, 3, 1]

for _ in range(int(input())):
    score = 0
    a, b, c, d, e, f, g, *data = list(map(int, input().split()))

    # 農田
    if a in (0, 1):
        score -= 1
    elif a > 5:
        score += 4
    else:
        score += a - 1

    # 圈地
    if b == 0:
        score -= 1
    elif b >= 4:
        score += 4
    else:
        score += b
    
    # 小麥
    if c == 0:
        score -= 1
    elif c in (1, 2, 3):
        score += 1
    elif c in (4, 5):
        score += 2
    elif c in (6, 7):
        score += 3
    else:
        score += 4

    # 蔬菜
    if d == 0:
        score -= 1
    elif d >= 4:
        score += 4
    else:
        score += d

    # 羊
    if e == 0:
        score -= 1
    elif e in (1, 2, 3):
        score += 1
    elif e in (4, 5):
        score += 2
    elif e in (6, 7):
        score += 3
    else:
        score += 4

    # 豬
    if f == 0:
        score -= 1
    elif f in (1, 2):
        score += 1
    elif f in (3, 4):
        score += 2
    elif f in (5, 6):
        score += 3
    else:
        score += 4

    # 牛
    if g == 0:
        score -= 1
    elif g == 1:
        score += 1
    elif g in (2, 3):
        score += 2
    elif g in (4, 5):
        score += 3
    else:
        score += 4

    # [空地, 圈地內馬廄, 磚屋, 石屋, 家庭成員, 紅利]
    for i in range(6):
        score += table[i] * data[i]

    print(score)
