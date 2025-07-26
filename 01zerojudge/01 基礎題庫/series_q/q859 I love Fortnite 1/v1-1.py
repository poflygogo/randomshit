# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q859. I love Fortnite 1


data = [
    "Aspect of Combat",
    "Ringmaster Scarr",
    "Night Rose",
    "Aspect of Speed",
    "Shrouded Striker",
    "Unstoppable",
    "Aspect of Siphon",
    "Infernal Defenses",
    "The Machinist",
    "Shogun X",
    "Megalo Don",
    "Aspect of Agility",
]

while True:
    try:
        print(data[int(input()) % 12])
    except EOFError:
        break
