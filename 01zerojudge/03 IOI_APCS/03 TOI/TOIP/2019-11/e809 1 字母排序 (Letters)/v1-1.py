# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e809. 1.字母排序 (Letters)
# 2019-11 TOI 練習賽 潛力組


text = input()
arr = sorted(input(), key=lambda x: text.index(x))
for _ in range(int(input())):
    print(arr[int(input()) - 1])
