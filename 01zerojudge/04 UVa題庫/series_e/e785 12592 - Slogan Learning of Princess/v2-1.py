# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12592 Slogan Learning of Princess
# ZeroJudge e785


slogan1 = []
slogan2 = []
for _ in range(int(input())):
    slogan1.append(input())
    slogan2.append(input())

for _ in range(int(input())):
    print(slogan2[slogan1.index(input())])
