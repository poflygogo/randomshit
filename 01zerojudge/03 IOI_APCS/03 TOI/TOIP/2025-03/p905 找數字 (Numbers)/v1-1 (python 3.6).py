# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p905. 找數字 (Numbers)
# TOI 練習賽 新手組


from math import sqrt, floor


def is_prime(n: int):
    if n == 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, floor(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def find_next_prime(n: int):
    if n <= 3:
        return (2, 3, 5)[n - 1]
    t = (1, 4, 3, 2, 1, 2)
    n += t[n % 6]
    while not is_prime(n):
        n += t[n % 6]
    return n


def find_next_square(n: int):
    return (floor(sqrt(n)) + 1) ** 2


def find_next_cube(n: int):
    # binary search to find cqrt
    low, high = 1, floor(sqrt(n))
    while low < high:
        mid = (low + high) // 2
        mid_cube = mid ** 3
        if mid_cube >= n:
            high = mid
        else:
            low = mid + 1

    # check the answer
    result = low ** 3
    if result == n:
        return (low + 1) ** 3
    else:
        return result


def main():
    ans = []
    n = int(input())
    ans.append(find_next_prime(n))
    ans.append(find_next_square(n))
    ans.append(find_next_cube(n))
    print(*ans)


if __name__ == '__main__':
    main()
