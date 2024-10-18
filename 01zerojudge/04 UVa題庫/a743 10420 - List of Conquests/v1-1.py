from sys import stdin


counter = {}
for _ in range(int(stdin.readline().rstrip())):
    country = stdin.readline().split().pop(0)
    counter[country] = counter.get(country, 0) + 1

for i in sorted(counter):
    print(i, counter[i])
