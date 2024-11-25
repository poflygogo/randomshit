# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a786. 8. 1337 XL8T0RZ
# HP CodeWars 2008


input()
l337 = [input().split(':')]
while True:
    text = input()
    if text == '[1337]':
        break
    l337.append(text.split(':'))

l337 = dict(l337)

while True:
    text = input()
    if text == '[3ND]':
        break
    print(*[l337[key] if key in l337 else key for key in text.split()])
