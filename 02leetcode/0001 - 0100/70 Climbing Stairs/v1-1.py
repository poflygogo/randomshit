class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        @cache
        def fib(n):
            if n < 3:
                return (0, 1, 2)[n]
            return fib(n - 1) + fib(n - 2)
        return fib(n)
