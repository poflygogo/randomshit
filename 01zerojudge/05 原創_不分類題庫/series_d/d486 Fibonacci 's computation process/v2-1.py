# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJungle d486. Fibonacci 's computation process


from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def gen_fib_tree(nums: list):
    print(' '.join(f'f({i})' for i in nums))
    if all(i < 2 for i in nums):
        return
    temp = []
    for i in range(len(nums)):
        if nums[i] < 2:
            temp.append(nums[i])
        else:
            temp.extend([nums[i] - 1, nums[i] - 2])
    return gen_fib_tree(temp)


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        gen_fib_tree([n])
        print(f'f({n}) = {fibonacci(n)}', end='\n\n')


if __name__ == '__main__':
    main()
