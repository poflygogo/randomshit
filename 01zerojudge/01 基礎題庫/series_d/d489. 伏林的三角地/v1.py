a, b, c = sorted(map(int, input().split()))

# 套用海龍公式
s = sum((a, b, c))/2
print(int(s * (s-a) * (s-b) * (s-c)))