# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12592 Slogan Learning of Princess
# ZeroJudge e785


slogan = {input().rstrip():input().rstrip() for _ in range(int(input()))}
for _ in range(int(input())):
    print(slogan[input().rstrip()])
