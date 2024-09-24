n = int(input())
data = [int(i) for i in input().split()]
flag = [False] * n    # 用來確認是否已經被處理過
count = 0

for num in range(n):
    if flag[num]: continue

    count += 1
    while not flag[num]:
        flag[num] = True
        num = data[num]

print(count)
