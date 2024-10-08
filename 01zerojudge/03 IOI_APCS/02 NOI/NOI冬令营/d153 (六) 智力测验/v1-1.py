from statistics import median_low
from sys import stdin


for _ in range(int(stdin.readline().rstrip())):
    print(
        median_low(int(stdin.readline().rstrip()) for i in range(int(stdin.readline().rstrip())))
    )
