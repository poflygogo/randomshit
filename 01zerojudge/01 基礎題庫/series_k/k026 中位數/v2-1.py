n = int(input()) / 2
data = [int(i) for i in input().split()]
print(
    data[int(n)] if not n.is_integer()
    else f'{(data[int(n)] + data[int(n) - 1]) / 2:g}'
)
