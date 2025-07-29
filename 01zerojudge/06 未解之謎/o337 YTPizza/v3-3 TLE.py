# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o337. YTPizza


n = int(input())
num, ipt = input().strip().split(maxsplit=1)
num = int(num)
seen = {num}
print(num, end=' ')
for _ in range(n - 2):
    num, ipt = ipt.split(maxsplit=1)
    num = int(num)
    if num not in seen:
        seen.add(num)
        print(num, end=' ')

ipt = int(ipt)
if ipt not in seen:
    print(ipt, end=' ')
