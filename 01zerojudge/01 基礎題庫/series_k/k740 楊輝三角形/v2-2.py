n = int(input())
pascals = [[1] * (i + 1) for i in range(n)]

for row in range(1, n):
    for col in range(1, row):
        pascals[row][col] = pascals[row - 1][col - 1] + pascals[row - 1][col]

for i in pascals:
    print(*i)
