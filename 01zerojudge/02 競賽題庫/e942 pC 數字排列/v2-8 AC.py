# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge e942. pC. 數字排列
# 2009大學學測推甄申請二階


from array import array
from sys import stdout


def dfs(path: array):
    if path and len(path) == n:
        stdout.write(' '.join(map(lambda x: str(nums[x]), path)) + '\n')
        return
    for i in range(n):
        if i not in path:
            path.append(i)
            dfs(path)
            path.pop()


n = int(input())
nums = array('q', sorted(map(int, input().split())))
dfs(array('q', []))
