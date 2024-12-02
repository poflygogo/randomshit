# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a862. 2. My Dear Friend VIR
# HP CodeWars 2010


from decimal import Decimal


while True:
    try:
        v, r = map(Decimal, input().split())
    except EOFError:
        break
    else:
        print(f'{1000 * v / r:.4f}')
