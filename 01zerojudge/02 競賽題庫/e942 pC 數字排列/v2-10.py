# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge e942. pC. 數字排列
# 2009大學學測推甄申請二階


def dfs(path: dict, depth: int = 0):
    if depth == n:
        print(*sorted(path, key=lambda x: path[x]))
        return
    for i in nums:
        if i not in path:
            path[i] = depth
            dfs(path, depth + 1)
            path.pop(i)


n = int(input())
nums = input().split()
nums.sort(key=int)
dfs({})
