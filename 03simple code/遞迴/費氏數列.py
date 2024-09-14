"""
目標: 求第 n 個費波納契數

fib(1) = 1
fib(2) = 1
fib(3) = 2
...
fib(n) = fib(n - 1) + fib(n - 2)
"""


def fib1(n: int) -> int:
    """for 循環"""
    if n <= 2:
        return 1
    prev1, prev2 = 1, 1
    for _ in range(3, n + 1):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2


def fib2(n: int) -> int:
    """遞迴"""
    if n <= 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


if __name__ == '__main__':
    num = 5
    print(
        f'fib1: {fib1(num)}',
        f'fib2: {fib2(num)}',
        sep='\n'
    )