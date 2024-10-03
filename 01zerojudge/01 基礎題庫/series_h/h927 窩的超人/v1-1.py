n, m = map(int, input().split())
a = input()
b = input()

lft = b.count('1')
rgt = m - lft

print(
    int('1' * lft + a + '0' * rgt, 2) % 998244353
)
