for i in range(int(input())):
    data = tuple(map(int, input().split()))
    if data[0] == 1:print(data[1] + data[2])
    elif data[0] == 2:print(data[1] - data[2])
    elif data[0] == 3:print(data[1] * data[2])
    else:print(int(data[1] / data[2]))
