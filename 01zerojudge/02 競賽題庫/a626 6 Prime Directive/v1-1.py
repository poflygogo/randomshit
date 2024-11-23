# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a626. 6. Prime Directive
# HP CodeWars 2007


from itertools import zip_longest


# 埃拉托斯特尼質數篩法
is_prime = [True] * 1001
primes = []
is_prime[0], is_prime[1] = False, False

for i in range(2, 1001):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 1001, i):
            is_prime[j] = False


while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        # 二分搜找最大的質數
        lft, rgt = 0, len(primes)
        while lft < rgt:
            mid = (lft + rgt) // 2
            if primes[mid] == n:
                rgt = mid + 1
                break
            elif primes[mid] < n:
                lft = mid + 1
            else:
                rgt = mid
        
        # more-itertools.grouper
        iterators = [iter(primes[:rgt])] * 5
        for line in zip_longest(*iterators):
            print(''.join(str(i).rjust(10) for i in line if i is not None))
