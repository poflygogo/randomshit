# 我是ㄌㄌㄎ

n, k, m = map(int, input().split())
if m >= n:
    input()
    print(0)
    exit()

matrix = [[int(i) for i in input().split()] + [0]]
for row in range(k):
    matrix.append([matrix[row][i] ^ matrix[row][i + 1] for i in range(n)] + [0])
print(matrix[k][m])
