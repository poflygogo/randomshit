# python 3.12
# ZeroJudge p912. 茶飲 (Tea)
# TOI 練習賽 202509 新手組 第1題

p, d, t, c = map(int, input().split())
if (d >= 30 and c == 0) or (d <= 15 and c == 1):
    p -= 5
if (7 <= t < 10) or (14 <= t < 16):
    p -= 5
print(p)
