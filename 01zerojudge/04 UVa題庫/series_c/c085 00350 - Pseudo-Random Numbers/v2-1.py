from sys import stdin


times = 0
for line in stdin:
    z, i, m, l = [int(i) for i in line.rstrip().split()]
    if z == i == m == l == 0:
        exit()

    times += 1
    flag = [0] * 10000
    count = 1
    while not flag[l]:
        flag[l] = count
        l = (z * l + i) % m
        count += 1

    print(f'Case {times}: {count - flag[l]}')
