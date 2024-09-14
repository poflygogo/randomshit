for _ in range(int(input())):
    total, diff = map(int, input().split())
    a = (total + diff) / 2
    b = total - a
    if (abs(a - b)) == diff and (a >= 0 and b >= 0) and a.is_integer() and b.is_integer():
        print(f'{a:.0f} {b:.0f}')
    else:
        print('impossible')
