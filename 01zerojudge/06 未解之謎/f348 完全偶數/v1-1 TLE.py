# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f348. 完全偶數


n = m = int(input())
even = '02468'

cnt = 0
while any(i not in even for i in str(n)) and any(i not in even for i in str(m)):
    cnt += 2
    n -= 2
    m += 2

print(cnt)
