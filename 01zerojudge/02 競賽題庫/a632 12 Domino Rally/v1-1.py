# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a632. 12. Domino Rally
# HP CodeWars 2007


# domino_id generator
# domino_id = {}
# n = 1
# for i in range(7):
#     for j in range(i, 7):
#         domino_id[n] = (i, j)
#         n += 1

from sys import stdin


domino_id = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (0, 3), '5': (0, 4), '6': (0, 5), '7': (0, 6), 
    '8': (1, 1), '9': (1, 2), '10': (1, 3), '11': (1, 4), '12': (1, 5), '13': (1, 6), '14': (2, 2),
    '15': (2, 3), '16': (2, 4), '17': (2, 5), '18': (2, 6), '19': (3, 3), '20': (3, 4), '21': (3, 5),
    '22': (3, 6), '23': (4, 4), '24': (4, 5), '25': (4, 6), '26': (5, 5), '27': (5, 6), '28': (6, 6)
 }

domino = []
for line in stdin:
    line = line.rstrip().split()
    if line[0] == '0':
        if domino:
            print(' '.join(i[0] for i in domino))
        else:
            print('DATASET CLEARED')
            
        domino.clear()
        continue

    domino.append((line[0], (domino_id[line[0]] if line[1] == 'F' else tuple(reversed(domino_id[line[0]])))))

    if len(domino) >= 2 and domino[-1][1][0] == domino[-2][1][1]:
        del domino[-2:]
