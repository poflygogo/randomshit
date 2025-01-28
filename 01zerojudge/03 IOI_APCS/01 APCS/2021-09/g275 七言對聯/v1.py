for _ in range(int(input())):
    data = [tuple(map(int, input().split())) for _ in range(2)]
    result = []

    # rule A
    for line in data:
        if line[1] != line[5] or line[1] == line[3]:
            result.append('A')
            break
    
    # rule B
    if data[0][6] == 0 or data[1][6]:
        result.append('B')
    
    # rule C
    if data[0][1] == data[1][1] or data[0][3] == data[1][3] or data[0][5] == data[1][5]:
        result.append('C')

    if result:
        print(*result, sep='')
    else:
        print('None')