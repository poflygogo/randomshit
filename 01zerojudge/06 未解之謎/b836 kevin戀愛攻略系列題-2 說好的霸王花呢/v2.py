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