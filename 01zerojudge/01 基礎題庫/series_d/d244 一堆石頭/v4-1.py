data = input().split()
counter = {}
for i in data:
    counter[i] = counter.get(i, 0) + 1 
print(max(counter, key=lambda x: counter[x] % 3))
