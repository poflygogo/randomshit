while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    if m == 0:
        print('Go Kevin!!')
        continue

    t = 0
    while True:
        check = (m * t ** 2 + (2 - m) * t) / 2
        if check < n:
            t += 1
        elif check == n:
            print('Go Kevin!!')
            break
        else:
            print('No Stop!!')
            break
