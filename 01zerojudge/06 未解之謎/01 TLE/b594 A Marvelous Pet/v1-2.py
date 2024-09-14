# from sys import stdin


stdin = open('test.txt')
for n in stdin:
    n = int(n)
    if not n: break

    check = 0
    count = 0
    for max_k in range(n // 2 + 1, 0, -1):
        for min_k in range(max_k - 1, 0, -1):
            if (max_k + min_k) * (max_k - min_k + 1) // 2 == n:
                count += 1
    print(f'{n:3d}: {count}')
