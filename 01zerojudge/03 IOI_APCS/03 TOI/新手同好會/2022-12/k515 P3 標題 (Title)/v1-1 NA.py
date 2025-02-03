# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k515. P3.標題 (Title)
# 2022-12 TOI 新手同好會


special_cases = {'the', 'a', 'an', 'in', 'on', 'at', 'of', 'for', 'by', 'to', 'and', 'or', 'but'}
text = input().split()
for i in range(len(text)):
    if i in (0, len(text) - 1) or text[i] not in special_cases:
        text[i] = text[i].capitalize()
print(' '.join(text))
