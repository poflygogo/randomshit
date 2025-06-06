# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e927. pA. 字串排序
# 2015大學學測推甄申請二階


text = input().rstrip()
text_counter = {}
for i in text:
    text_counter[i] = text_counter.get(i, 0) + 1
print(''.join(chr(i) * text_counter[chr(i)] for i in range(65, 91)))
