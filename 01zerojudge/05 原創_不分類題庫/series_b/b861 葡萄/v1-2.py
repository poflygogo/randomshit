for _ in range(int(input())):
    flag = False
    count_chi = 0
    for i in input().split():
        if i == 'chi':
            count_chi += 1
        else:
            count_chi -= 1
            if count_chi < 0 and not flag:
                flag = True

    if flag:
        if count_chi > 0:
            print("chi pu tao bu tu pu tao pi, bu chi pu tao dao tu pu tao pi")
        else:
            print("bu chi pu tao dao tu pu tao pi")
    elif count_chi > 0:
        print("chi pu tao bu tu pu tao pi")
    else:
        print("chi pu tao tu pu tao pi")
