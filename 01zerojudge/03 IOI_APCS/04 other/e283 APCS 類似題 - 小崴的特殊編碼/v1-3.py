from sys import stdin


key = {
    5: 'A',
    7: 'B',
    2: 'C',
    13: 'D',
    8: 'E',
    12: 'F'
}


for i in stdin:
    print(
        *[key[int(''.join(stdin.readline().rstrip().split()), 2)] for _ in range(int(i.rstrip()))],
        sep=''
    )
