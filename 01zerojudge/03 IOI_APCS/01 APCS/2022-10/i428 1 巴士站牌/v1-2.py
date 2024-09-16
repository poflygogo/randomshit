n = int(input()) - 2
a, b = map(int, input().split())
pre_a, pre_b = map(int, input().split())
length = abs(pre_a - a) + abs(pre_b - b)
max_num, min_num = length, length
for _ in range(n):
    a, b = map(int, input().split())
    length = abs(pre_a - a) + abs(pre_b - b)
    if length > max_num:
        max_num = length
    elif length < min_num:
        min_num = length
    pre_a, pre_b = a, b

print(max_num, min_num)
