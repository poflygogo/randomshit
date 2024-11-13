from sys import stdin

for data in stdin:
    data = list(map(int, data.split()))
    length = data.pop(0)
    for idx in range(length - 1):
        if not (1 <= abs(data[idx] - data[idx + 1]) <= length):
            print('Not jolly')
            break
    else:
        print('Jolly')