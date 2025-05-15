# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b309. 聖杯戰爭


from sys import stdin

servant = ["Saber", "Lancer", "Archer", "Rider", "Caster", "Assassin", "Berserker"]
counter = {chr(i + 65): 0 for i in range(10)}
for text in stdin:
    for i in text.upper():
        if i.isalpha():
            counter[chr((ord(i) - 65) % 7 + 65)] += 1

print(servant[ord(max(counter, key=lambda x: (counter[x], -ord(x)))) - 65])
