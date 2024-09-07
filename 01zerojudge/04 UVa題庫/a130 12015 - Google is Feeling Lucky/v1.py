for case in range(int(input())):
    data = [input().split() for _ in range(10)]
    max_weight = max({int(i[1]) for i in data})
    data = [i[0] for i in data if int(i[1]) == max_weight]
    print(
        f'Case #{case + 1}:',
        *data,
        sep='\n'
    )