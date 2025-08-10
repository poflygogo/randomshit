# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1376. Time Needed to Inform All Employees

from typing import List
import collections


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        graph = collections.defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)
        result = 0

        def dfs(curr: int, time: int = 0):
            if curr not in graph:
                nonlocal result
                if result < time:
                    result = time
                return
            time += informTime[curr]
            for employee in graph[curr]:
                dfs(employee, time)
        
        dfs(headID)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]))
