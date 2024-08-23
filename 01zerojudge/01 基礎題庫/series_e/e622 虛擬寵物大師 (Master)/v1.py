pokemon, sand = map(int, input().split())
sand //= 1000

data_cp = []
for _ in range(pokemon):
    cp, iv = map(int, input().split())
    if iv < 30: iv = 10
    elif iv < 40: iv = 50
    else: iv = 100
    cp += iv * sand
    data_cp.append(cp)

result = max(data_cp)
print(data_cp.index(result) + 1, result)