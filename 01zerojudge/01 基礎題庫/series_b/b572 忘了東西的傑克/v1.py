for _ in range(int(input())):
    h1, m1, h2, m2, run = map(int, input().split())
    m1 += h1 * 60
    m2 += h2 * 60
    if m2 - m1 >= run:
        print('Yes')
    else:
        print('No')