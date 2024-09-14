"""
目標: 傳入一個正整數 n，求 n! 的結果
"""


def func1(n: int) -> int:
    """for 循環"""
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


def func2(n: int) -> int:
    """遞迴"""
    if n == 1:
        return 1
    return n * func2(n - 1)


if __name__ == '__main__':
    num = 5
    print(
        f'func1: {func1(num)}',
        f'func2: {func2(num)}',
        sep='\n'
    )
