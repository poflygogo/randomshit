# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a869. 9. Letter Scramble
# HP CodeWars 2010


scramble = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
    'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
    'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

data = [input().split() for _ in range(int(input()))]

for _ in range(int(input())):
    text, row, col, direct = input().split()
    row, col = map(lambda n: int(n) - 1, (row, col))
    word_mul = 1
    score = 0
    for i, chr in enumerate(text):
        if direct == 'H':
            curr = data[row][col + i]
        else:
            curr = data[row + i][col]
        
        score += scramble[chr] * (int(curr[0]) if curr[1] == 'L' else 1)
        if curr[1] == 'W':
            word_mul *= int(curr[0])
    score *= word_mul
    print(text, score)
