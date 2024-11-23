# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a625. 5. Overhanging Cards
# HP CodeWars 2007


while True:
    try:
        n = float(input())
    except EOFError:
        break
    else:
        count = 1
        harmonic = 0.5

        while n > harmonic:
            count += 1
            harmonic += 1 / (count + 1)
        
        print(count, 'card(s)')
