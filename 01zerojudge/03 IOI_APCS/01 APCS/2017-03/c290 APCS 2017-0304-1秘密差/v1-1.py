data = input().strip()
print(
    abs(
        sum([int(i) for i in data[::2]]) -
        sum([int(i) for i in data[1::2]])
    )
)
