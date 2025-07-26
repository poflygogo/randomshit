# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e265. 拱豬


# ---------------------------------------------------

import sys
import io

Q = """
2
AH 2H 3H 4H #
5H 6H 7H 8H #
9H TH JH QH KH QS #
JD TC #
AH 2H 3H 4H 5H 6H 7H 8H 9H TH JH QH KH QS #
#
#
JD TC #
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


card_info = {
    "AH": -50,
    "KH": -40,
    "QH": -30,
    "JH": -20,
    "QS": -100,
    "JD": 100,
    "TH": -10,
}
card_info.update({f"{i}H": -10 for i in range(5, 10)})


TOTAL_PLAYER = 4
scores_final = [0] * TOTAL_PLAYER
for round in range(1, int(input()) + 1):
    scores = [0] * TOTAL_PLAYER
    small_slam = False  # 豬羊變色
    for player in range(TOTAL_PLAYER):
        arr = input().split()
        arr.pop()   # 移除最後面的 "#"

        heart_cnt = 0
        double = False
        for card in arr:
            if card[1] == "H":
                heart_cnt += 1
            if card == "TC":
                double = True
            scores[player] += card_info.get(card, 0)
        if heart_cnt == 13:
            small_slam = True
        if double:
            scores[player] *= 2
    if small_slam:
        for i in range(TOTAL_PLAYER):
            scores[i] *= -1

    print(
        f"Round {round}:",
        "\n".join(f"  {i + 1}: {scores[i]}" for i in range(TOTAL_PLAYER)),
        sep="\n",
    )
    for i in range(TOTAL_PLAYER):
        scores_final[i] += scores[i]

print(
    "Final:",
    "\n".join(f"  {i + 1}: {scores_final[i]}" for i in range(TOTAL_PLAYER)),
    sep="\n",
)
