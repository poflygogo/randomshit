arm_num_list = []
a, b = map(int, input().split())
for i in range(a, b+1):
    i_str = str(i)
    i_length = len(i_str)
    check = 0
    for j in i_str:
        check += int(j) ** i_length
    if i == check:
        arm_num_list.append(i)
if len(arm_num_list) == 0: print('none')
else:print(*arm_num_list)
