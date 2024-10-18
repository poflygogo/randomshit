a, b, c, base = map(int, input().split())

aa = a // base if a % base == 0 else 0
bb = b // base if b % base == 0 else 0
cc = c // base if c % base == 0 else 0

print(aa * bb * cc)

# 測資未公開
# 2024-10-18
# AC(24ms, 3.3MB)
