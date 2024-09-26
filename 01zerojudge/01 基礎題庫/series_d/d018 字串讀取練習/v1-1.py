while True:
    try:
        data = [[float(j) for j in i.split(':')] for i in input().split()]
    except EOFError:
        break

    print(f'{sum(i[1] for i in data if i[0] % 2 != 0) - sum(i[1] for i in data if i[0] % 2 == 0): <g}')
