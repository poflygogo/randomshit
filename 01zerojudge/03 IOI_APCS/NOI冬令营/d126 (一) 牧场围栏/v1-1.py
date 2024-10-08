from sys import stdin


for line in stdin:
    print(int.__add__(*map(int, line.rstrip().split())) * 2)
