from sys import stdin


key = {
    '0 1 0 1': 'A',
    '0 1 1 1': 'B',
    '0 0 1 0': 'C',
    '1 1 0 1': 'D',
    '1 0 0 0': 'E',
    '1 1 0 0': 'F'
}


for i in stdin:
    print(
        ''.join([key[stdin.readline().rstrip()] for _ in range(int(i.rstrip()))]),
    )
