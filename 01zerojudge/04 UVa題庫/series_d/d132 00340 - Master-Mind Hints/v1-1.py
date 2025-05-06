# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00340 Master-Mind Hints
# ZeroJudge d132


from collections import defaultdict


def master_mind(length: int, target: tuple, target_counter: dict, guess: list) -> tuple:
    a = b = 0
    guess_counter = counter(guess)
    for i in range(length):
        if target[i] == guess[i]:
            a += 1
    b = sum(min(target_counter[i], guess_counter[i]) for i in target_counter) - a
    return a, b


def counter(arr):
    result = defaultdict(int)
    for i in arr:
        result[i] = result.get(i, 0) + 1
    return result


def main():
    game = 1
    n = int(input())
    while n:
        print(f'Game {game}:')
        target = tuple(map(int, input().split()))
        target_counter = counter(target)
        guess = list(map(int, input().split()))
        while any(guess):
            a, b = master_mind(n, target,target_counter ,guess)
            print(f'    ({a},{b})')
            guess = list(map(int, input().split()))
        game += 1
        n = int(input())


if __name__ == '__main__':
    main()
