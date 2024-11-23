# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a622. 2. Vertical Printing
# HP CodeWars 2007


from itertools import zip_longest


name = []
while True:
    text = input()
    if text == 'END':
        break
    name.append(text)

for i in zip_longest(*name, fillvalue=' '):
    print(*i, sep='  ')
