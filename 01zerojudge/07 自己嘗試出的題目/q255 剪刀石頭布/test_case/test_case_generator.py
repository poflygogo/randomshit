# -*- encoding: utf-8 -*-
# python 3.12


import random


def solve_the_problem() -> str:
    pass


def setup_files(n: int, range_a: int, range_b: int, end: int, start: int = 0, invalid_mode: bool = False):
    file_in = open()
    file_in


def generate_problem():
    setup_files(n=random.sample(range(1, 10), 5),
                range_a=0,
                range_b=0,
                start=0,
                end=5)
    setup_files(n=random.sample(range(10, 100), 5),
                range_a=0,
                range_b=int(10e4),
                start=5,
                end=8)
    setup_files(n=random.sample(range(10, 100), 5),
                range_a=0,
                range_b=2 ** 32,
                start=8,
                end=10)


if __name__ == '__main__':
    generate_problem()
