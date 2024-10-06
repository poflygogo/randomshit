from functools import reduce
from operator import sub, mul, truediv, pow


data = [int(i) for i in input().split()]
result = data.pop()
if sum(data) == result:
    print('+')
if reduce(sub, data) == result:
    print('-')
if reduce(mul, data) == result:
    print('*')
if reduce(truediv, data) == result:
    print('/')
if reduce(pow, data) == result:
    print('**')
