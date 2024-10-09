from sys import stdin


key = {
    '0101': 'A',
    '0111': 'B',
    '0010': 'C',
    '1101': 'D',
    '1000': 'E',
    '1100': 'F'
}


for i in stdin:
    print(
        *[key[''.join(stdin.readline().rstrip().split())] for _ in range(int(i.rstrip()))],
        sep=''
    )
