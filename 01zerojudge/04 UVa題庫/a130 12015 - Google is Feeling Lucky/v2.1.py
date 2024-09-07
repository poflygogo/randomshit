for case in range(int(input())):
    data = {}
    for _ in range(10):
        website = input().split()
        data[int(website[1])] = data.get(int(website[1]), []) + [website[0]]
    print(
        f'Case #{case + 1}:',
        *data[max(data)],
        sep='\n'
    )