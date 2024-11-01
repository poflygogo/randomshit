from functools import reduce
from operator import mul


# python 3.12 要添加下面這兩行
# import sys
# sys.set_int_max_str_digits(10000)


num = [1]
for i in range(2, 101):
    num.append(num[-1] * i)
result = reduce(mul, num)
print('\n'.join(i for i in str(result)))
