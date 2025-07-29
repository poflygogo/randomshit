# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o337. YTPizza


input()
ipt = input().strip()

last = 0
idx = ipt.find(" ", last)
while idx != -1:
    num = ipt[last:idx]
    if ipt.find(num, 0, last) == -1:
        if last > 0:
            print(' ', end='')
        print(num, end='')
    last = idx + 1
    idx = ipt.find(' ', last)

num = ipt[last:]
if ipt.find(num, 0, last) == -1:
    if last > 0:
        print(' ', end='')
    print(num)
