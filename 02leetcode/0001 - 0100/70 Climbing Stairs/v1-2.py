class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return (0, 1, 2)[n]
        prev1, prev2 = 1, 2
        n -= 2
        while n:
            prev1, prev2 = prev2, prev1 + prev2
            n -= 1
        return prev2
