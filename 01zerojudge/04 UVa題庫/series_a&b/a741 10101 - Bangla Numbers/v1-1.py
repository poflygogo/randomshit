# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10101 Bangla Numbers
# ZeroJudge a741


BANGLA_UNITS = {"kuti": 10000000, "lakh": 100000, "hajar": 1000, "shata": 100}

def bangla_number(n: int) -> str:
    for name in BANGLA_UNITS:
        if n >= BANGLA_UNITS[name]:
            a, b = divmod(n, BANGLA_UNITS[name])
            if b == 0:
                return f'{bangla_number(a)} {name}'
            else:
                return f'{bangla_number(a)} {name} {bangla_number(b)}'
    return str(n)


t = 1
while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(f'{t:>4d}. {bangla_number(n)}')
    t += 1
