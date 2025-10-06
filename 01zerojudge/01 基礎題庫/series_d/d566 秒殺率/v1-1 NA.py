from sys import stdin


data = {}
_ = next(stdin)
for line in stdin:
    a, b = line.strip().split()
    if a in data:
        if b == 'AC':
            data[a][0] = True
        continue
    if b == 'AC':
        data[a] = [True, True]
    else:
        data[a] = [False, False]

result = sum(1 for i in data.values() if i[1]) / sum(1 for i in data if data[i][0]) * 100
print(f'{result:.0f}%')
