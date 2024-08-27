n, m = map(int, input().split())

data = [input().strip() for _ in range(n)]
data = ''.join(data)

print(
    *[data[key - 1] for key in tuple(map(int, input().split()))],
    sep=''
)