input()
data = {int(j): i + 1 for i, j in enumerate(input().split())}

for query in (int(i) for i in input().split()):
    print(data.get(query, 0))
