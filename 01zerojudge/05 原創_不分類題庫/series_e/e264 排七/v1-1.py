# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e264. 排七


# 其實我也不知道我在寫三小，總之能動了

from typing import Optional, Iterator


class Pile:
    def __init__(self):
        self.lower = 7
        self.upper = 7
    
    def __repr__(self):
        return f"{self.lower}, {self.upper}"


card_value = {j: i + 1 for i, j in enumerate("A23456789TJQK")}
category = "CDHS"


def _add_exception(target_set: set, piles: dict):
    for i in category:
        if i not in piles:
            target_set.add(f"7{i}")
            continue
        if piles[i].upper < 13:
            target_set.add(f"{piles[i].upper + 1}{i}")
        if piles[i].lower > 1:
            target_set.add(f"{piles[i].lower - 1}{i}")


def _can_be_insert(target: str, piles: dict):
    if target[0] == '7':
        return True
    if target[1] not in piles:
        return False
    if card_value[target[0]] in (piles[target[1]].upper + 1, piles[target[1]].lower - 1):
        return True
    return False


def find_cheater(n: int, record: list, cover: Optional[Iterator] = None, result: str = "No one"):
    piles = {}
    should_not_appear = {i: set() for i in range(4)}
    for idx in range(n):
        if record[idx] == "XX":
            if cover is None:
                cover = iter(input().split())
            item = next(cover)
            if _can_be_insert(item, piles):
                return str(idx % 4 + 1)
            _add_exception(should_not_appear[idx % 4], piles)

        elif record[idx] in should_not_appear[idx % 4]:
            return str(idx % 4 + 1)

        # same as record[idx][0] == "7"
        elif record[idx][1] not in piles:
            piles[record[idx][1]] = Pile()

        elif card_value[record[idx][0]] > piles[record[idx][1]].upper:
            piles[record[idx][1]].upper += 1

        else:
            piles[record[idx][1]].lower -= 1
    return result


# ------main------
while True:
    n = int(input())
    if n == 0:
        break

    record = input().split()
    result = find_cheater(n, record)
    print(f"{result} cheated!")
