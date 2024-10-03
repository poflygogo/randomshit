length = int(input())
data = input().split()

i, cnt = 0, 0
while i < length:
    if data[i] == '0':
        i += 1
        continue

    else:
        cnt += 1
        i += 2
print(cnt)
