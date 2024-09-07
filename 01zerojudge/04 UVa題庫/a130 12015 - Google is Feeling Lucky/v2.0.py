for case in range(int(input())):
    data = {}
    for _ in range(10):
        website = input().split()
        weight = int(website[1])
        data[weight] = data.get(weight, []) + [website[0]]
    print(
        f'Case #{case + 1}:',
        *data[max(data)],
        sep='\n'
    )