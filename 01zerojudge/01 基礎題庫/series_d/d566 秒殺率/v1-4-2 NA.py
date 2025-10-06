from sys import stdin


data = {}
f = stdin.readlines()
del f[0]
for line in f:
    a, b = line.strip().split()
    data[a] = data.get(a, []) + [b == 'AC']

result = sum(1 for i in data if data[i][-1]) * 100 // sum(1 for i in data if True in data[i])
print(f'{result}%')
