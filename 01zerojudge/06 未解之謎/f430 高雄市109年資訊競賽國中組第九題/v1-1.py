# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge f430. 高雄市109年資訊競賽國中組第九題
# 2020高雄市資訊學科能力複賽109高雄市資訊學科能力複賽
# 
# greedy 似乎不行呢...要 dp


from fractions import Fraction as frac


n, m = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(n)]

data.sort(key=lambda x: -x[0] / sum(x))

# 候選人 x
temp = data[:m]
result = frac(sum(i[0] for i in temp), sum(sum(i) for i in temp))
print(int(result) if result.is_integer() else f'{result.numerator}/{result.denominator}')

# 候選人 y
