data = [[1]]
for row in range(1, int(input())):
    temp = []
    for col in range(row + 1):
        if col in (0, row):
            temp.append(1)
        else:
            temp.append(data[row - 1][col - 1] + data[row - 1][col])
    data.append(temp)
for i in data:
    print(*i)
