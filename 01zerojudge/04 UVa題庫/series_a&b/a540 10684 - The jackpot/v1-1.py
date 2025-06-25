# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10684 - The jackpot
# ZeroJudge a540


import sys

for n_line in sys.stdin:
    n = int(n_line.strip())

    if n == 0:
        break

    bets = list(map(int, sys.stdin.readline().strip().split()))

    # Kadane's algorithm
    max_streak = 0
    current_streak = 0
    for bet in bets:
        current_streak += bet
        if current_streak < 0:
            current_streak = 0
        max_streak = max(max_streak, current_streak)

    if max_streak > 0:
        print(f"The maximum winning streak is {max_streak}.")
    else:
        print("Losing streak.")
