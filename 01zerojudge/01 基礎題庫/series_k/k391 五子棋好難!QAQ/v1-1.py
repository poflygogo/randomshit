a = input().split()
b = input().split()

print(
    'tie' if a[1] == b[1]
    else f'{max(a, b, key=lambda x: int(x[1]))[0]} WIN!'
)
