length, _ = map(int, input().split())
data = [int(i) for i in input().split()]

for query in (int(i) for i in input().split()):
    if query in data:
        print(data.index(query) + 1)

    else:
        print(0)      
