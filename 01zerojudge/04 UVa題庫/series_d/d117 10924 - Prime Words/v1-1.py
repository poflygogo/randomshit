# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10924 Prime Words

from sys import stdin


for line in stdin:
    word_value = sum(ord(char) - 38 if char.isupper() else ord(char) - 96 for char in line.rstrip())

    def is_prime(n: int) -> bool:
        if n in (1, 2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for p in range(5, int(n ** 0.5) + 1, 6):
            if n % p == 0 or n % (p + 2) == 0:
                return False
        return True

    print(f'It is {"" if is_prime(word_value) else "not "}a prime word.')
