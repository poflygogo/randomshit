# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a780. 2. Magnificent Views
# HP CodeWars 2008


while True:
    fo, fe, fa = map(float, input().split())
    if fo == fe == fa == 0:
        break

    print(f'{fo / fe:.2f} {fa / fo * fe:.2f}')
