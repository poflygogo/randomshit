# 遞迴又遞迴的 lambda
# 可正常執行，最後會輸出 6

print((lambda main: main(main, 3))(lambda hard, arg: 0 if arg == 0 else arg + hard(hard, arg - 1)))



# -----------------
# 拆開來後大概是這個形式
from typing import Callable

def func_a(main: Callable):
    return main(main, 3)

def func_b(hard: Callable, arg: int) -> int:
    if arg == 0:
        return 0
    else:
        return arg + hard(hard, arg - 1)

print(func_a(func_b))


# -----------------
# 然而實際邏輯是這樣
def func_c(arg: int):
    if arg == 0:
        return 0
    else:
        return arg + func_c(arg - 1)

print(func_c(3))


# -----------------
# 再具體一點，就只是累加而已
def func_d(arg: int):
    result = 0
    for i in range(arg + 1):
        result += i
    return result

print(func_d(3))


# who the fuck code like this?????
