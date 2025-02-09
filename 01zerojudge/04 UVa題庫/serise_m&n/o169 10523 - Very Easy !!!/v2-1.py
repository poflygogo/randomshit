# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10523 Very Easy !!!
# ZeroJudge o169


from sys import stdin

for line in stdin:
    n, a = map(int, line.rstrip().split())
    arr = [0] * n
    arr[0] = a
    for i in range(1, n):
        arr[i] = arr[i - 1] * a
    print(sum(arr[i] * (i + 1) for i in range(n)))
