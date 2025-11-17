# python 3.12
# ZeroJudge p914. 完美數 (Perfect)
# TOI 練習賽 202509 新手組 第3題


n = int(input())
factors_sum = 1
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        factors_sum += i
        if (t := n // i) != i:
            factors_sum += t

print(factors_sum, f"{('not ', '')[factors_sum == n]}perfect", sep="\n")
