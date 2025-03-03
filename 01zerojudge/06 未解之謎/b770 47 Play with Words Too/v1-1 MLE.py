# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b770. 47. Play with Words, Too.


# ---------------------------------------------------

import sys
import io
Q = """
print
insert left g 2
insert right e 1
insert 3 l 1
insert 2 o 2
print
insert 4 o 25
print
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------

from sys import stdin
from itertools import groupby, compress, repeat
from collections import deque


def operate(text: deque, comm: str):
    if comm.startswith('insert left'):
        _, x, n = comm.rsplit(maxsplit=2)
        text.extendleft([x] * int(n))
    elif comm.startswith('insert right'):
        _, x, n = comm.rsplit(maxsplit=2)
        text.extend([x] * int(n))
    elif comm.startswith('insert'):
        _, k, x, n = comm.split()
        k, n = int(k), int(n)
        text.rotate(-(k - 1))
        text.extendleft([x] * n)
        text.rotate(k - 1)
    else:
        print_context(text)


def print_context(text: deque):
    print(' '.join([f'{i} {ilen(j)}' for i, j in groupby(text)] + ['$']))


def ilen(iterable) -> int:
    """ Return the number of items in *iterable*

        This consumes the iterable, so handle with care.
        see more: https://more-itertools.readthedocs.io/en/stable/_modules/more_itertools/more.html#ilen
    """
    return sum(compress(repeat(1), zip(iterable)))


def main():
    text = deque()
    for command in stdin:
        operate(text, command.rstrip())


if __name__ == '__main__':
    main()
