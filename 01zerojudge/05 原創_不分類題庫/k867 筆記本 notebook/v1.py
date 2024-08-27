data = input().split()
order = map(lambda i: int(i) - 1, input().split())
result = sorted(zip(data, order), key= lambda i: i[1])
print(
    *[i[0] for i in result]
)