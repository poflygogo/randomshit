# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a790. 12. Haunted House Inspector
# HP CodeWars 2008

# -------------------------------------------------------------------

import sys
import io

Q = """ 60 9 84
        #############S##############################################
        #FFFFFF FF        #FFF           #       #   #FF    #  FFFF#
        ############### # #### ####### # #### #### ######## ######F#
        # F F  FFFFF FFF#  FF#       # # #FFFF   #  F#      #FFFFFF#
        ##########F#### # ############ # ####### # ### ######F######
        #               #  FFFFFFF   # # #FFFF   #  F#      #FFFFFF#
        ##########F####F# ############ # ####### # ### ###########F#
        #  FFF  FFFFF       FFFFFFFF   #                     FFFFFF#
        ############################################################
        60 9 84
        #############S##############################################
        #FFFFFF FF        #FFF           #       #   #FF    #  FFFF#
        ############### # #### ####### # #### #### ######## ######F#
        # F F  FFFFF FFF#  FF#       # # #FFFF   #  F#      #FFFFFF#
        ##########F#### # ############ # ####### # ### ######F######
        #               #  FFFFFFF   # # #FFFF   #  F#      #FFFFFF#
        ##########F####F# ############ # ####### # ### ###########F#
        #  FFF  FFFFF       FFFFFFFF   #                     FFFFFF#
        ############################################################
    """
sys.stdin = io.StringIO(Q.rstrip())

# -------------------------------------------------------------------

from collections import deque


def find_entrance():
    for i in range(max_row):
        for j in range(max_col):
            if graph[i][j] == 'S':
                return i, j

DR = (-1, 0, 0, 1)
DC = (0, -1, 1, 0)

while True:
    try:
        max_col, max_row, pipe = map(int, input().split())
    except EOFError:
        break

    graph = [list(input().strip()) for _ in range(max_row)]
    r, c = find_entrance()
    queue = deque([(r, c, 1)])
    seen = set((r, c))
    while queue:
        r, c, length = queue.popleft()
        graph[r][c] = '.'
        if length == pipe:
            continue
        length += 1
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if (nr, nc) not in seen and 0 <= nr < max_row and 0 <= nc < max_col and graph[nr][nc] != '#':
                seen.add((nr, nc))
                queue.append((nr, nc, length))
    
    print('\n'.join(''.join(i) for i in graph))
    if all(j != 'F' for i in graph for j in i):
        print('\nAll Fires Extinguished!')
