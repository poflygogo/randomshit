"""
印出 2000-01-01 到 2999-12-31 間所有的質數日
"""
import random


def is_prime(n: int, k: int = 3):
    if n in (3, 7, 13, 17, 23, 29):
        return True

    """Miller-Rabin"""
    # 一開始要先把 n-1 變成 2^s*d 的格式
    s = 0
    d = n - 1

    # 當 d 還有因數 2 時，就把 2 抽出來
    while d % 2 == 0:
        s += 1
        d = d >> 1  # 相當於 d //= 2

    for i in range(k):                  # k 值代表要執行幾次，次數越多越準確，但效率就越差
        a = random.randint(2, n - 1)    # 從這個範圍內隨機挑選一個數字
        if not is_possible_prime(n, a, s, d):
            return False
    
    return True


def is_possible_prime(n, a, s, d):
    # pow(a, d, n) = a ^ d % n
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    
    for _ in range(s - 1):
        x = x ** 2 % n
        if x == n - 1:
            return True

    return False


for year in range(2000, 3000):
    for month in range(1, 13):
        for day in (3, 7, 13, 17, 23, 29):
            date = str(year) + str(month).zfill(2) + str(day).zfill(2)
            for i in range(8):
                if not is_prime(int(date[i:])):
                    break
            else:
                print(f'{year}/{month:0>2d}/{day:0>2d}')
