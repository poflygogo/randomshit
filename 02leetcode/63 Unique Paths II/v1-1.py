# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 63. Unique Paths II


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                item = obstacleGrid[r - 1][c - 1]
                if item == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r - 1][c] + dp[r][c - 1]
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
