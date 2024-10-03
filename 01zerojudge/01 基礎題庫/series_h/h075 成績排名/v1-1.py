from sys import stdin


data_raw, data_avg = {}, []
for _ in range(int(stdin.readline().rstrip())):
    stu, s1, s2, s3 = map(int, stdin.readline().rstrip().split())
    data_raw[stu] = (s1, s2, s3)
    data_avg.append((stu, sum(i * j for i, j in zip(data_raw[stu], (5, 3, 2))) / 10))

data_avg.sort(key=lambda x: (x[1], data_raw[x[0]], -x[0]), reverse=True)
for i, j in data_avg:
    print(f'{i} {j:g}')
