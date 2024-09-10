for _ in range(int(input())):
    x, y, z, w, n, m = map(int, input().split())
    eat = {'0': 0, '1': x, '2': y, '3': -z, '4': -w}
    action = input().split()

    poison = 0
    for i in action:
        m -= n * poison
        if m <= 0: break
        m += eat[i]
        if m <= 0: break
        if i == '4': poison += 1

    print(f'{m}g' if m > 0 else 'bye~Rabbit')
