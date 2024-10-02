from sys import stdin


def linear_sieve(n: int) -> list:
    flag = [True] * (n + 1)         # 初始化 list
    primes = []                     # 保存質數
    flag[0] = flag[1] = False       # 把 0 和 1 都設定成 False
    for i in range(2, n + 1):
        if flag[i]:                 # 如果是 True 就視為質數
            primes.append(i)

        for p in primes:
            if p * i > n:           # list index out of range
                break
            flag[p * i] = False     # 把對應的數字標記為合數
            if i % p == 0:          # 確保每個合數只被篩一次
                break
    return primes


def binary_search(n):
    lft, rgt = 0, length
    while lft <= rgt:
        mid = (lft + rgt) // 2
        if prime[mid] == n:
            return mid + 1
        if prime[mid] > n:
            rgt = mid - 1
        else:
            lft = mid + 1


limit, cases = map(int, stdin.readline().rstrip().split())
prime = linear_sieve(limit)
length = len(prime) - 1
for _ in range(cases):
    print(binary_search(int(stdin.readline().rstrip())))
