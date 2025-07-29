# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o337. YTPizza


input()
ipt = input().strip()

seen = set()
last = 0
idx = ipt.find(" ", last)
while idx != -1:
    num = int(ipt[last:idx])
    if num not in seen:
        if seen:
            print(' ', end='')
        print(num, end='')
        seen.add(num)
    last = idx + 1
    idx = ipt.find(' ', last)

num = int(ipt[last:])
if num not in seen:
    if seen:
        print(' ', end='')
    print(num, end='')
