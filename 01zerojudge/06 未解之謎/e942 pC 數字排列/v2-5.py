# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge e942. pC. 數字排列
# 2009大學學測推甄申請二階


from array import array


def dfs(path: array, visit: set):
    if visit and path and len(path) == n:
        print(*path)
        return
    for i in range(n):
        if i not in visit:
            path.append(nums[i])
            visit.add(i)
            dfs(path, visit)
            path.pop()
            visit.remove(i)


n = int(input())
nums = array('q', sorted(map(int, input().split())))
dfs(array('q', []), set())
