num, tgt = map(int, input().split())

cnt = 0
for i in range(1, num + 1):
    while i > 0:
        if i % 10 == tgt:
            cnt += 1
        i //= 10

print(cnt)