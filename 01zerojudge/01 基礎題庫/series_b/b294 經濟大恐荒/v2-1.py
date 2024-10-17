# 不需要知道有幾筆資料
input()

data = input().split()
print(sum((i + 1) * int(j) for i, j in enumerate(data)))
