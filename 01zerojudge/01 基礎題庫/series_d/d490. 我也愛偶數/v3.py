a, b = map(int, input().split())

# 等差數列和公式
a += a % 2
b -= b % 2
print((a + b) * ((b - a) //2 + 1) // 2)