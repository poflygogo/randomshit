# HP CodeWars2010
from sys import stdin


for line in stdin:
    a, b = map(int, line.strip().split())
    print((a + b) * 2)
