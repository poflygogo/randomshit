data = input().strip()
length = len(data)
print(
    abs(
        sum([int(data[i]) for i in range(0, length, 2)]) -
        sum([int(data[i]) for i in range(1, length, 2)])
    )
)
