from sys import stdin


for i in stdin:
    a, b, c, d = map(int, i.rstrip().split())
    print(f'{pow(a, b, pow(c, d)): <3,}'.replace(',', ' '))
