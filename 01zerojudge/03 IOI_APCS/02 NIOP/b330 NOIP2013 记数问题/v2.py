num, tgt = input().split()

cnt = 0
for i in range(1, int(num) + 1):
    cnt += str(i).count(tgt)

print(cnt)