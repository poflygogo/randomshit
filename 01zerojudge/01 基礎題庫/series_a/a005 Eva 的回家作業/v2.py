# 有病的三行解

for _ in range(int(input())):
    data = [int(i) for i in input().split()]
    print(
        *data,
        data[-1] + data[1] - data[0] if data[1] - data[0] == data[2] - data[1] else data[-1] * (data[1] // data[0])
    )
