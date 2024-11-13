for _ in range(int(input())):
    length = int(input())
    carts = [int(i) for i in input().split()]
    cnt = 0

    for _ in range(length - 1):
        for i in range(length - 1):
            if carts[i] > carts[i + 1]:
                carts[i], carts[i + 1] = carts[i + 1], carts[i]
                cnt += 1

    print(f'Optimal train swapping takes {cnt} swaps.')
