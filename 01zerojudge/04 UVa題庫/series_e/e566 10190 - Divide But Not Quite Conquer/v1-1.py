# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10190 Divide, But Not Quite Conquer!
# zerojudge e566


def div_but_not_conquer(n: int, m: int) -> str:
    if m == 0 or m == 1 or n % m != 0:
        return 'Boring!'
    result = [n]
    while n > 1:
        n //= m
        if n != 1 and n % m != 0:
            return 'Boring!'
        result.append(n)
    return ' '.join(str(i) for i in result)


while True:
    try:
        print(div_but_not_conquer(*map(int, input().split())))
    except EOFError:
        break
