# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a865. 5. Greek Numerals
# HP CodeWars 2010


ionian = {
    'A': 1, 'B': 2, 'G': 3, 'D': 4, 'E': 5, '#': 6, 'Z': 7, 'Y': 8, 'H': 9,
    'I': 10, 'K': 20, 'L': 30, 'M': 40, 'N': 50, 'X': 60, 'O': 70, 'P': 80, 'Q': 90,
    'R': 100, 'S': 200, 'T': 300, 'U': 400, 'F': 500, 'C': 600, '$': 700, 'W': 800, '3': 900
}

while True:
    ionian_num = input().rstrip()
    if ionian_num == '.':
        break
    print(sum(ionian[i] for i in ionian_num))
