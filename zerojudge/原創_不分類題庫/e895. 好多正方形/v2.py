from sys import stdin

for line in stdin:
    print(pow(2, (int(line) - 1), 10007))