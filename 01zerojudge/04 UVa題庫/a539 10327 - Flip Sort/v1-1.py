from sys import stdin


for n in stdin:
    n = int(n.rstrip())
    data = [int(i) for i in next(stdin).rstrip().split()]
    cnt = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                cnt += 1
    print(f'Minimum exchange operations : {cnt}')
