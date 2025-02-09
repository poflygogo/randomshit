# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11991 Easy Problem from Rujia Liu?
# ZeroJudge n802


from sys import stdin

for line in stdin:
    n, m = map(int, line.rstrip().split())
    arr = stdin.readline().rstrip().split()
    arr_dict = {}
    for i in range(n):
        arr[i] = int(arr[i])
        arr_dict[arr[i]] = arr_dict.get(arr[i], []) + [i + 1]
    for _ in range(m):
        k, v = map(int, stdin.readline().rstrip().split())
        if v in arr_dict and k <= len(arr_dict[v]):
            print(arr_dict[v][k - 1])
        else:
            print(0)
