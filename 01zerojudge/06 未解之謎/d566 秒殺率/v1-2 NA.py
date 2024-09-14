from sys import stdin


data = {}
_ = next(stdin)
for line in stdin:
    a, b = line.strip().split()
    data[a] = data.get(a, []) + [b == 'AC']

result = sum(1 for i in data if data[i][0]) * 100 // sum(1 for i in data if True in data[i])
print(f'{result}%')
