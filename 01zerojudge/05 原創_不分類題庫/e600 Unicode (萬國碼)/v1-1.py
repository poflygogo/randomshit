# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e600. Unicode (萬國碼)


from sys import stdin


for s in stdin:
    s = s.rstrip()
    c = chr(int(s[2:], base=16))
    print(*[bin(i)[2:] for i in c.encode()])
    print(c)
