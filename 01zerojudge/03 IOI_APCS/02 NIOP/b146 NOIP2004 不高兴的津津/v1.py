data = {}
for i in range(1, 8):
    a, b = map(int, input().split())
    data[i] = a + b
print(
    max(
        data,
        key= lambda x: data[x]
    )
)