from math import sqrt


while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    if m == 0:
        print('Go Kevin!!')
        continue

    check = ((2 - m) ** 2 + 8 * n * m)
    if check < 0:
        print('No Stop!!')
        continue

    check = sqrt(check)
    if not check.is_integer():
        print('No Stop!!')
        continue

    check1, check2 = m - 2 + check, m - 2 - check
    if check1 % (2 * m) == 0 or check2 % (2 + m) == 0:
        print('Go Kevin!!')
    else:
        print('No Stop!!')
