def fib(n: int, temp: dict={}) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in temp:
        return temp[n]
    temp[n] = fib(n - 1, temp) + fib(n - 2, temp)
    return temp[n]


print(fib(int(input())))
