for _ in range(int(input())):
    length = int(input())
    carts = [int(i) for i in input().split()]
    cnt = 0
    flag = False    # 紀錄該次循環是否有發生交換

    for i in range(length - 1):
        flag = False
        for j in range(length - 1 - i):
            if carts[j] > carts[j + 1]:
                carts[j], carts[j + 1] = carts[j + 1], carts[j]
                cnt += 1
                flag = True

        # 若有發生交換，便提早退出循環
        if not flag:
            break

    print(f'Optimal train swapping takes {cnt} swaps.')
