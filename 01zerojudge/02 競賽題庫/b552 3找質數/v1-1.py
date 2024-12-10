# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b552. 3.找質數
# 103學年度北二區桃竹苗基區資訊學科能力競賽


primes = {2, 3, 5, 7, 11, 13, 17,19}


def is_prime(n: int) -> bool:
    """判斷是否為質數(試除法/輪式篩法)"""
    global primes
    if n == 1:
        return False
    if n in primes:
        return True
    if any(n % p == 0 for p in primes):
        return False
    for p in range(5, int(n ** 0.5) + 1, 6):
        if n % p == 0 or n % (p + 2) == 0:
            return False
    primes.add(n)
    return True


while True:
    try:
        ipt = input().rstrip()
    except EOFError:
        break
    else:
        idx_s, idx_e = 0, 1
        result = []
        while idx_e <= 10:
            num = int(ipt[idx_s:idx_e])
            if is_prime(num):
                result.append(num)
                idx_s, idx_e = idx_e, idx_e + 1
            else:
                idx_e += 1
        print(len(result), *result, sep='\n', end='\n\n')
