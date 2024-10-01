"""
印出 2000-01-01 到 2999-12-31 間所有的質數日
"""
import math


def is_prime(n: int):
    if n in (3, 7, 13, 17, 23, 29):
        return True
    if n % 3 == 0:
        return False
    
    max_factor = math.sqrt(n)
    if max_factor.is_integer():
        return False
    for p in range(5, math.ceil(max_factor), 6):
        if n % p == 0 or n % (p + 2) == 0:
            return False
    return True


for year in range(2000, 3000):
    for month in range(1, 13):
        for day in (3, 7, 13, 17, 23, 29):
            date = str(year) + str(month).zfill(2) + str(day).zfill(2)
            for i in range(8):
                if not is_prime(int(date[i:])):
                    break
            else:
                print(f'{year}/{month:0>2d}/{day:0>2d}')
