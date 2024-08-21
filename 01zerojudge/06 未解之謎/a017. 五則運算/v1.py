equation = list(map(lambda n: int(n) if n.isnumeric() else n ,input().split()))

idx = 0
while len(equation) == 1:
    # 檢查是數字還是符號，是符號就跳過
    if type(equation[idx]) == int:
        idx += 1
        continue

    symbol = equation[idx]