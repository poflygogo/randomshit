from sys import stdin

for data in stdin:
    data = list(map(int, data.split()))
    length = data.pop(0)
    diff = set()
    for i in range(length - 1):
        d = abs(data[i] - data[i + 1])
        if (1 <= d < length) and (d not in diff):
            diff.add(d)
    if len(diff) == length - 1:
        print('Jolly')
    else:
        print('Not jolly')