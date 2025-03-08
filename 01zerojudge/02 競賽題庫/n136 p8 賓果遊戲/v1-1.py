# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n136. p8. 賓果遊戲


n = int(input())
nums = set(map(int, input().split()))
bingo = [list(map(int, input().split())) for _ in range(5)]

a = b = 0

for r in range(5):
    t = sum(bingo[r][c] in nums for c in range(5))
    if t == 5:
        a += 1
    elif t == 4:
        b += 1

for c in range(5):
    t = sum(bingo[r][c] in nums for r in range(5))
    if t == 5:
        a += 1
    elif t == 4:
        b += 1

t = sum(bingo[i][i] in nums for i in range(5))
if t == 5:
    a += 1
elif t == 4:
    b += 1

t = sum(bingo[i][4-i] in nums for i in range(5))
if t == 5:
    a += 1
elif t == 4:
    b += 1

print(a, b)
