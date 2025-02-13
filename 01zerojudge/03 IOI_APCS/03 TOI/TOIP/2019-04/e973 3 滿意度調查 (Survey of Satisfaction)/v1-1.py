# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e973. 3. 滿意度調查 (Survey of Satisfaction)
# 2019-04 TOI 練習賽 新手組


from collections import Counter

text_counter = Counter(input().rstrip())
print(' '.join(sorted(text_counter.keys(), key=lambda x: (-text_counter[x], int(x)))))
