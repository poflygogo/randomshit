"""
根據題目要求，使用遞迴
"""

from sys import stdin


def factorial(n: int):
    if n in (0, 1):     # 如果 n 是 1 或 0，就直接返回 1
        my_list.append(1)
        return 1
    my_list.append(n)
    return n * factorial(n - 1)


for n in stdin:
    n = int(n)
    my_list = []        # 用來保存計算過程
    ans = factorial(n)
    print(
        f'{n}!',
        '=',
        " * ".join(map(str, my_list)),
        '=',
        ans
    )
