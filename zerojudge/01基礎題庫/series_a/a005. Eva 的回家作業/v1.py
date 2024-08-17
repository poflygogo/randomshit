list_count = int(input())

for count in range(list_count):
    check_list = [int(x) for x in input().split()]
    if check_list[1] - check_list[0] == check_list[2] - check_list[1]:
        check_list.append(check_list[3] * 2 - check_list[2])
    else:
        check_list.append(check_list[3] ** 2 // check_list[2])
    print(*check_list)
