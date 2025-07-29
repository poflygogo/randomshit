# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o337. YTPizza


input()
ipt = input().strip()

seen = set()
idx = ipt.find(" ")
while idx != -1:
    num = ipt[:idx]
    ipt = ipt.lstrip(num).strip()
    num = int(num)
    if num not in seen:
        seen.add(num)
        print(num, end=" ")
    idx = ipt.find(" ")

num = int(ipt)
if num not in seen:
    print(num, end=" ")
