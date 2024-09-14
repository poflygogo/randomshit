# from sys import stdin

f = open(r'test.txt', 'r', encoding="utf-8")
data: dict[str, list] = {}
_ = next(f)
for line in f:
    a, b = line.strip().split()
    data[a] = data.get(a, []) + [True if b == 'AC' else False]

result = sum(1 for i in data if data[i][0]) * 100 // sum(1 for i in data if True in data[i])
print(f'{result}%')
