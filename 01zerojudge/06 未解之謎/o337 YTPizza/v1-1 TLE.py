# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o337. YTPizza

from sys import stdin

read = lambda: stdin.read(1)

input()

seen = set()
num = 0
t: str = read()
while t:
    if t.isdigit():
        num = num * 10 + int(t)
    elif num not in seen:
        if seen:
            print(" ", end="")
        print(num, end="")
        seen.add(num)
        num = 0
    else:
        num = 0
    t = read()


if num not in seen:
    if seen:
        print(" ", end="")
    print(num)
