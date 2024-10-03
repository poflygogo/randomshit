from sys import stdin


data = []
for _ in range(int(stdin.readline().rstrip())):
    stu, s1, s2, s3 = map(int, stdin.readline().rstrip().split())
    data.append((stu, s1, s2, s3, sum(i * j for i, j in zip((s1, s2, s3), (5, 3, 2))) / 10))
data.sort(key=lambda x: (x[4], x[1], x[2], x[3], -x[0]), reverse=True)

for i in data:
    print(f'{i[0]} {i[4]:g}')
