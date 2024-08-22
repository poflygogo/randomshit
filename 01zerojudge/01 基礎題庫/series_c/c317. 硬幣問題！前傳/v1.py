from sys import stdin, stdout

_ = stdin.readline()
for line in stdin:
    cost, curr_a, curr_b = map(int, line.strip().split())

    a = 0
    while cost >= curr_a:
        a += 1
        cost -= curr_a