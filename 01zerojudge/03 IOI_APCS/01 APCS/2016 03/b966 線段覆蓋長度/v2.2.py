length = int(input())
data = [tuple(map(int, input().split())) for _ in range(length)]
data.sort()

cnt, sta, end = 0, 0, 0
for a, b in data:
    if a <= end:
        if b <= end:
            continue
        else:
            end = b
    else:
        cnt += end - sta
        sta, end = a, b
cnt += end - sta
print(cnt)