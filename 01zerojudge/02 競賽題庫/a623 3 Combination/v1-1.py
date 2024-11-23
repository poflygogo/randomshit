# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a623. 3. Combination
# HP CodeWars 2007


def factorial(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


while True:
    try:
        n, m = map(int, input().split())
    
    except EOFError:
        break

    else:
        print(factorial(n) // (factorial(m) * factorial(n - m)))
