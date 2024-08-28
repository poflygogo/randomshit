data = [input() for _ in range(5)]
for i in range(5):
    print(*[data[j][i] for j in range(5)], sep='')