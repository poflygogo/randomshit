from sys import setrecursionlimit

setrecursionlimit(2147483647)

a = {True : lambda x:0,         # 若 x == 0，不再遞迴，而是直接返回數值
     False : lambda x:func(x)}  # 若 x != 0，就持續遞迴

def func(x):
    return x + a[x == 0](x-1)

print(func(int(input())))
