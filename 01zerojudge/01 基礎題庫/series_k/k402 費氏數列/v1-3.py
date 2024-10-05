def fib(n: int, temp=None) -> int:
    if not temp:
        temp = {1: 0, 2: 1}
    if n in temp:
        return temp[n]
    temp[n] = fib(n - 1, temp) + fib(n - 2, temp)
    return temp[n]


print(fib(int(input())))
