# 我是ㄌㄌㄎ

n, k, m = map(int, input().split())
if m >= n:
    input()
    print(0)
    exit()

if m == n - 1:
    print(int(input().split()[-1]))
    exit()

matrix = [int(i) for i in input().split()]
for _ in range(k):
    matrix = [matrix[i] ^ matrix[i + 1] for i in range(n - 1)] + matrix[-1:]
print(matrix[m])
