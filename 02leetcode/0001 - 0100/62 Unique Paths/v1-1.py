# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 62. Unique Paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                dp[r][c] += dp[r - 1][c] + dp[r][c - 1]
        return dp[r][c]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
