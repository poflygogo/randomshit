# -*- encoding: utf-8 -*-
# python 3.12
# UVa 156 - Ananagrams
# ZeroJudge q897


data = {}
while True:
    line = input().strip()
    if line == "#":
        break
    for s in line.split():
        t = "".join(sorted(s.upper()))
        if t in data:
            data[t][0] = False
        else:
            data[t] = [True, s]

print("\n".join(sorted(s for flag, s in data.values() if flag)))
