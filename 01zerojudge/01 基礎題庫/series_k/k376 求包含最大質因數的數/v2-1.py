def linear_sieve(n: int) -> list:
    # 初始化
    primes = []                     # 用來存放所有質數
    is_prime = [True] * (n+1)       # is_prime[i] 表示 i 是否為質數
    min_prime_factor = [0] * (n+1)  # 最小質因子

    # 從 2 開始篩
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)         # 如果 i 是質數，加入質數列表
            min_prime_factor[i] = i  # i 本身是最小的質因子

        # 枚舉質數去篩掉合數
        for p in primes:
            if p * i > n:            # 超出範圍
                break
            is_prime[p * i] = False  # 標記合數
            min_prime_factor[p * i] = p  # 記錄最小質因子

            if i % p == 0:           # 保證每個合數只會被最小的質因子篩掉
                break

    return primes


def max_prime_factor(n: int) -> int:
    """
    取最大的質因數

    :param n: 要檢查的數字
    :return: 最大的質因數
    """
    factors = []
    for i in prime:
        if n % i == 0:
            factors.append(i)
    return max(factors) if factors else n


prime = linear_sieve(1229)
data = [int(input()) for _ in range(int(input()))]
print(max(data, key=max_prime_factor))
