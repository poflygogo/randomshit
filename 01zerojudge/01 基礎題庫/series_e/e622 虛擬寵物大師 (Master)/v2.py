pokemon, sand = map(int, input().split())
sand //= 1000

data_cp = []
for _ in range(pokemon):
    cp, iv = map(int, input().split())
    if iv < 30:
        data_cp.append(10 * sand + cp)
    elif iv < 40:
        data_cp.append(50 * sand + cp)
    else:
        data_cp.append(100 * sand + cp)

result = max(data_cp)
print(data_cp.index(result) + 1, result)