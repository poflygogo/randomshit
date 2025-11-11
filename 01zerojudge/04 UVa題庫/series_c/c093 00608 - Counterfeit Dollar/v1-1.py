# python 3.12
# UVa 00608 Counterfeit Dollar
# ZeroJudge c093

from typing import List, Tuple, Literal


class Test:
    def __init__(self, lft: str, rgt: str, status: str):
        self.lft = lft
        self.rgt = rgt
        self.flag = ("up", "even", "down").index(status) - 1

    def is_possible(self, char: str, val: Literal[1, -1]):
        w1 = sum(val * (i == char) for i in self.lft)
        w2 = sum(val * (i == char) for i in self.rgt)
        res = 1 if w1 < w2 else 0 if w1 == w2 else -1
        return res == self.flag


Result = Tuple[str, Literal["heavy", "light"]]

def solve(data: List[Test], total_char: int = 12) -> Result:
    for i in range(total_char):
        char = chr(ord("A") + i)
        if all(i.is_possible(char, 1) for i in data):
            return char, "heavy"
        if all(i.is_possible(char, -1) for i in data):
            return char, "light"

    return "Z", "heavy"  # should not happen


def main():
    T = 3
    for _ in range(int(input())):
        data = [Test(*input().split()) for _ in range(T)]
        print("{} is the counterfeit coin and it is {}.".format(*solve(data)))


main()
