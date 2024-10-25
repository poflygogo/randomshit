from sys import stdin


times = 0
for line in stdin:
    times += 1
    z, i, m, l = map(int, line.rstrip().split())
    if z == i == m == l == 0:
        exit()

    cycle = [l]
    while True:
        new = (z * cycle[-1] + i) % m
        if new in cycle:
            break
        else:
            cycle.append(new)

    print(f'Case {times}: {len(cycle) - cycle.index(new)}')
