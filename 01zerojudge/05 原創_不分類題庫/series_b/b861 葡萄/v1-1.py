for _ in range(int(input())):
    data = [True if i == 'chi' else False for i in input().split()]
    flag_more_chi, flag_more_tu = False, False
    count_chi = 0
    for i in data:
        if i:
            count_chi += 1
        else:
            count_chi -= 1
            if count_chi < 0 and not flag_more_tu:
                flag_more_tu = True

    if flag_more_tu:
        if count_chi > 0:
            print("chi pu tao bu tu pu tao pi, bu chi pu tao dao tu pu tao pi")
        else:
            print("bu chi pu tao dao tu pu tao pi")
    elif count_chi > 0:
        print("chi pu tao bu tu pu tao pi")
    else:
        print("chi pu tao tu pu tao pi")
