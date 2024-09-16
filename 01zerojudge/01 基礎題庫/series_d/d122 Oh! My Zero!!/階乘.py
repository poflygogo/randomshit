def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    # 求 n! 的尾數共有幾個 0
    # 暴力解
    while True:
        num = factorial(int(input()))
        num = str(num)
        print(
            len(num) - len(num.rstrip('0'))
        )
