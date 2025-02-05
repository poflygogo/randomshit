# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge e942. pC. 數字排列
# 2009大學學測推甄申請二階


def dfs(path: list, visit: set):
    if visit and path and len(path) == n:
        print(*[nums[i] for i in path])
        return
    for i in offset:
        if i not in visit:
            path.append(i)
            visit.add(i)
            dfs(path, visit)
            path.pop()
            visit.remove(i)


n = int(input())
offset = tuple(range(n))
nums = list(map(int, input().split()))
nums.sort()
dfs([], set())
