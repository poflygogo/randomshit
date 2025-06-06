# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e927. pA. 字串排序
# 2015大學學測推甄申請二階


from collections import Counter

text_counter = Counter(input().rstrip())
print(''.join(chr(i) * text_counter[chr(i)] for i in range(65, 91)))
