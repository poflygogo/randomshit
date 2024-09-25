input()
data = [int(i) for i in input().split()]
data.sort()
print(
    ' '.join(str(i) for i in data),
    ' '.join(map(str, sorted(list(set(data)), reverse=True))),
    sep='\n'
)
