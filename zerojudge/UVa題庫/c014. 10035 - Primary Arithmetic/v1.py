while True:
    a, b = input().split()
    if a == b == '0':
        break

    list_a = list(reversed([int(i) for i in a]))
    list_b = list(reversed([int(i) for i in b]))

    count = 0
    for index, item in enumerate(list_a):
        if (item + list_b[index]) // 10 != 0:
            count += 1
            if len(list_a)-1 == index:
                break
            else:
                list_a[index+1] += 1

    if count == 0:
        print(f'No carry operation.')
    elif count == 1:
        print(f'1 carry operation.')
    else:
        print(f'{count} carry operations.')
