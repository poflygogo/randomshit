# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJungle d486. Fibonacci 's computation process


def fibonacci(n: int) -> list:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp


def gen_fib_tree(nums: list):
    print(' '.join(f'f({i})' for i in nums))
    if all(i < 2 for i in nums):
        return
    i = 0
    while i < len(nums):
        if nums[i] < 2:
            i += 1
        else:
            nums[i] -= 1
            nums.insert(i + 1, nums[i] - 1)
            i += 2
    return gen_fib_tree(nums)


def main():
    fib_list = fibonacci(15)
    while True:
        n = int(input())
        if n == 0:
            break
        gen_fib_tree([n])
        print(f'f({n}) = {fib_list[n]}', end='\n\n')


if __name__ == '__main__':
    main()
