# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10101 Bangla Numbers
# ZeroJudge a741


BANGLA_UNITS = {"kuti": 10000000, "lakh": 100000, "hajar": 1000, "shata": 100}

def bangla_number(n: int) -> str:
    def calc(n: int) -> list:
        for name in BANGLA_UNITS:
            if n >= BANGLA_UNITS[name]:
                a, b = divmod(n, BANGLA_UNITS[name])
                temp = []
                temp.extend(calc(a))
                temp.append(name)
                if b != 0:
                    temp.extend(calc(b))
                return temp
        return [str(n)]
    return ' '.join(calc(n))


t = 1
while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(f'{t:>4d}. {bangla_number(n)}')
    t += 1
