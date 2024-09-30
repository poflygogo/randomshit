from math import gcd
from functools import reduce


while True:
    if input() == '0':
        break

    print(reduce(lambda a, b: a * b // gcd(a, b), map(int, input().split())))
