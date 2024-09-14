from sys import stdin


for line in stdin:
    m, k = map(int, line.strip().split())
    if not k:
        if m:
            print('Impossib1e!')
        else:
            print('Ok!')
    elif m % k == 0:
        print('Ok!')
    else:
        print('Impossib1e!')
