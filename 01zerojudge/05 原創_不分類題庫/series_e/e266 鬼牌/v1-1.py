# ZeroJudge e266. 鬼牌
# https://zerojudge.tw/ShowProblem?problemid=e266


# ---------------------------------------------------

import sys
import io

Q = """
5 AS AD 5D 5H TS
5 AS AD AC 5H TS
4 AS AD AC GG
8 AS AD 5D 5H TS TC TD TH
0
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


from typing import List

_weight = {j: i for i, j in enumerate("CDHSG")}
_card_val = {j: i for i, j in enumerate("A23456789TJQKG", start=1)}


def Joker(pile: List[str]) -> List[str]:
    pile.sort(key=lambda x: (_card_val[x[0]], _weight[x[1]]))
    idx = 0
    while len(pile) > 1 and idx < len(pile) - 1 and pile[idx] != "GG":
        if pile[idx][0] == pile[idx + 1][0]:
            del pile[idx : idx + 2]
        else:
            idx += 1
    return pile


def main():
    while True:
        cnt, *pile = input().split()
        if cnt == "0":
            break
        result = Joker(pile)
        if result:
            print(" ".join(result))
        else:
            print("No card")


main()
