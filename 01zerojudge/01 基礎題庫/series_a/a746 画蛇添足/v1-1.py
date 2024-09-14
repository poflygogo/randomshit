import sys


def generate_matrix(num: int) -> list:
    out = [['|'] + [' '] * num + ['|'] for _ in range(num)]
    out.insert(0, ['-' * (num + 2)])
    out.append(['-' * (num + 2)])
    return out


for line in sys.stdin:
    n, m = map(int, line.split())
    matrix = generate_matrix(n)
    queue = tuple(map(int, next(sys.stdin).split()))
    for _ in range(m - 1):
        data = tuple(map(int, next(sys.stdin).split()))
        if queue[0] == data[0]:
            if queue[1] < data[1]:
                a, b = queue[1], data[1] + 1
            else:
                a, b = data[1], queue[1] + 1
            for i in range(a, b):
                matrix[data[0]][i] = '*'
        else:
            if queue[0] < data[0]:
                a, b = queue[0], data[0] + 1
            else:
                a, b = data[0], queue[0] + 1
            for i in range(a, b):
                matrix[i][data[1]] = '*'
        queue = data
    [print(*i, sep='') for i in matrix]
