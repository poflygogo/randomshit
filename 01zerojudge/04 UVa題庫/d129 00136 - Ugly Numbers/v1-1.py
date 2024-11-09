# -*- uft-8 -*-
# python 3.12
# UVa 00136 Ugly Numbers
# LeetCode 264 Ugly Number II
# 效率很糟糕的暴力解

n, cnt = 15, 11
while cnt < 1500:
    n += 1

    def is_ugly_number(num: int) -> bool:
        for i in (2, 3, 5):
            while num % i == 0:
                num //= i
        return bool(num == 1)

    if is_ugly_number(n):
        cnt += 1

print(f"The 1500'th ugly number is {n}.")
