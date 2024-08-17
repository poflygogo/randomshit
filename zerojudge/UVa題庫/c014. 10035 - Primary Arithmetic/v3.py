def carry_operation(listA:list, listB:list) -> int:
    count = 0
    for index, item in enumerate(listA):
        if (item + listB[index]) // 10 != 0:
            count += 1
            if len(listA)-1 == index:
                break
            else:
                listA[index+1] += 1
    return count


while True:
    a, b = input().split()
    if a == b == '0':
        break

    list_a = list(reversed([int(i) for i in a]))
    list_b = list(reversed([int(i) for i in b]))

    if len(list_a) != len(list_b):
        if len(list_a) > len(list_b):
            list_b.extend([0]*(len(list_a)-len(list_b)))
        else:
            list_a.extend([0]*(len(list_b)-len(list_a)))
    
    count = carry_operation(list_a, list_b)

    if count == 0:
        print(f'No carry operation.')
    elif count == 1:
        print(f'1 carry operation.')
    else:
        print(f'{count} carry operations.')
