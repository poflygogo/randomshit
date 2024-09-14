from sys import stdin


data = {}
_ = next(stdin)
for line in stdin.readlines():
    a, b = line.strip().split()
    data[a] = data.get(a, []) + [b == 'AC']

result = sum(1 for i in data if data[i][-1]) * 100 // sum(1 for i in data if True in data[i])
print(f'{result}%')
