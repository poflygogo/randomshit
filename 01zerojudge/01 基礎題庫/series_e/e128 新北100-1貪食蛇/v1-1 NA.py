from math import sqrt


while True:
    n = int(input())
    if n == 0: break

    n_sqrt = sqrt(n)
    if n_sqrt.is_integer():
        if n_sqrt % 2:
            print(1, int(n_sqrt))
        else:
            print(int(n_sqrt), 1)

    else:
        n_sqrt = int(n_sqrt)
        mid = n_sqrt ** 2 + n_sqrt + 1
        if n_sqrt % 2:
            if n <= mid:
                print(n - n_sqrt, n_sqrt + 1)
            else:
                print(n_sqrt + 1, (n_sqrt + 1) ** 2 - n + 1)

        else:
            if n <= mid:
                print(n_sqrt + 1, n - n_sqrt ** 2)
            else:
                print((n_sqrt + 1) ** 2 - n + 1, n_sqrt + 1)
