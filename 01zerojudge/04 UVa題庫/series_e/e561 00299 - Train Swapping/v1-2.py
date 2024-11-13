for _ in range(int(input())):
    length = int(input())
    carts = [int(i) for i in input().split()]
    cnt = 0

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if carts[j] > carts[j + 1]:
                carts[j], carts[j + 1] = carts[j + 1], carts[j]
                cnt += 1

    print(f'Optimal train swapping takes {cnt} swaps.')
