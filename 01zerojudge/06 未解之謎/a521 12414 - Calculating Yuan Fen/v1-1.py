# python 3.12
# ZeroJudge a521
# UVa 12414 Calculating Yuan Fen

from typing import Dict, Union
from string import ascii_uppercase
from sys import stdin


class CalculatingYuanFen:
    def __init__(self):
        self.cache: Dict[str, int] = {}
        self.char_to_int: Dict[str, int] = {j: i for i, j in enumerate(ascii_uppercase)}
        self.min_limit = 1
        self.max_limit = 10000

    def _calc(self, s: str) -> int:
        if len(s) <= 2 or s == "100":
            return int(s)
        if self.cache.get(s, 0):
            return self.cache[s]
        s_next = "".join(str((int(i) + int(j)) % 10) for i, j in zip(s, s[1:]))
        self.cache[s] = self._calc(s_next)
        return self.cache[s]

    def solve(self, s: str) -> Union[int, str]:
        for st in range(self.min_limit, self.max_limit + 1):
            num_str = "".join(str(self.char_to_int[i] + st) for i in s)
            result = self._calc(num_str)
            if result == 100:
                return st
        return ":("


def main():
    solution = CalculatingYuanFen()
    for line in stdin:
        print(solution.solve(line.strip()))


main()
