def combinatorics(a: int, b: int) -> int:
    """
    求排列組合 C(a, b) C a 取 b 共有多少組合
    """
    if a < b or b == 0:
        return 0
    elif b == 1:
        return a
    elif a == b:
        return 1
    return combinatorics(a - 1, b - 1) + combinatorics(a - 1, b)


print(combinatorics(10, 5))
