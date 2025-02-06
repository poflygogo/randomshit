# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge e942. pC. 數字排列
# 2009大學學測推甄申請二階


from array import array


def dfs(path: array, visit: array):
    if visit and path and len(path) == n:
        print(*path)
        return
    for i in range(n):
        if not visit[i]:
            path.append(nums[i])
            visit[i] ^= 1
            dfs(path, visit)
            path.pop()
            visit[i] ^= 1


n = int(input())
nums = array('q', sorted(map(int, input().split())))
dfs(array('q', []), array('b', [0] * n))
