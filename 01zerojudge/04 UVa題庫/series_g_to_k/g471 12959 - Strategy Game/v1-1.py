# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12959 Strategy Game
# ZeroJudge g471


from sys import stdin

for line in stdin:
    players, rounds = map(int, line.rstrip().split())
    if players == rounds == 0:
        break
    get_scores = tuple(map(int, stdin.readline().rstrip().split()))
    
    scores = [sum(get_scores[j] for j in range(i, players * rounds, players)) for i in range(players)]
    print(max(enumerate(scores), key=lambda x: (x[1], x[0]))[0] + 1)
