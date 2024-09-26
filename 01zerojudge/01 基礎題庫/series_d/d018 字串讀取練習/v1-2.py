while True:
    try:
        data = [i.split(':') for i in input().split()]
    except EOFError:
        break

    print(f'{sum(float(i[1]) for i in data if int(i[0]) % 2 != 0) - sum(float(i[1]) for i in data if int(i[0]) % 2 == 0): <g}')
