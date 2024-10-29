from sys import stdin


def eratosthenes():
    """用埃篩獲取小於1000的質數列表，已知除了 2 以外的偶數都是合數，那就不需要再檢查，一開始就全部標記成合數"""
    is_prime = [False, True] * 500
    prime_list = [1, 2]
    for i in range(3, 999, 2):
        if is_prime[i]:
            prime_list.append(i)
            for j in range(i * i, 999, i):
                is_prime[j] = False
    return prime_list


primes = eratosthenes()
for line in stdin:
    line = line.rstrip()
    num, cut = map(int, line.split())

    # 二分搜尋找小於 num 的質數中最大的那個在什麼位置
    # lft - 1 就是最大的質數
    lft, rgt = 0, len(primes)
    while lft < rgt:
        mid = (lft + rgt) // 2
        if num < primes[mid]:
            rgt = mid
        else:
            lft = mid + 1

    # 根據 cut 的值決定要印出哪些質數
    if cut >= lft:
        print(line + ':', *primes[:lft])
    elif lft % 2 == 0:
        print(line + ':', *primes[lft // 2 - cut:lft // 2 + cut])
    else:
        print(line + ':', *primes[lft // 2 - cut + 1:lft // 2 + cut])
