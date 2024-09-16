from sys import stdin


n = int(stdin.readline().strip())
data = [tuple(map(int, i.strip().split())) for i in stdin]
manhattan = [abs(data[i][0] - data[j][0]) +
             abs(data[i][1] - data[j][1])
             for i, j in zip(range(n - 1), range(1, n))
             ]
print(max(manhattan), min(manhattan))
