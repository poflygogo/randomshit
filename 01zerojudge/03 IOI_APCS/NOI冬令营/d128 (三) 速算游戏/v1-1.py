from sys import stdin


for line in stdin:
    a, b, c = line.rstrip().split()
    
    cases = (
        sum(map(int, (a, b, c))),
        int(a) * int(b) * int(c),
        int(a) + int(b + c),
        int(a + b) + int(c),
        int(a) * int(b + c),
        int(a + b) * int(c),
        int(a) + int(b) * int(c),
        int(a) * int(b) + int(c),
    )
    print(max(cases))
