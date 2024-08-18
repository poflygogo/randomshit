from sys import stdin

for line in stdin:
    a, b, c = map(int, line.split())

    candidate = [('A', a), ('B', b), ('C', c)]
    candidate.sort(key= lambda n: n[1])

    if candidate[0][1] + candidate[1][1] > candidate[2][1]:
        print(candidate[1][0])
    else:
        print(candidate[2][0])