# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p911. 橋牌 (Bridge)
# TOI練習賽202506新手組第3題


foo = dict(zip("AKQJ", range(4, 0, -1)))
bar = "SHDC"
bar_cnt = {i: 0 for i in bar}
score = 0

for i in input().split():
    bar_cnt[i[0]] += 1
    score += foo.get(i[1], 0)

print(' '.join(str(bar_cnt[i]) for i in bar))
print(score)
