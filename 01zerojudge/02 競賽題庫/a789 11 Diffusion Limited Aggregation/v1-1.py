# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a789. 11. Diffusion Limited Aggregation
# HP CodeWars 2008


# ----------------------------------------------------
# replace input() data

import sys
import io

q = """ 600 809 840 815 555 508 493 546 608 737 930
        774 831 699 536 586 818 485 790 861 617 838
        799 919 538 521 510 431 924 742 589 602 814
        645 933 801 521 728 870 701 621 705 746 730
        665 665 655 515 496 720 729 969 517 858 532
        606 606 572 797 480 469 455 666 483 488 514
        545 864 928 866 906 639 454 480 699 607 582
        884 602 617 608 812 957 583 499 500 672 672
        966 597 587 580 958 667 684 537 500 912 805
        843 783 653 577 528 523 521 515 506 830 875
        643 904 632 859 627 690 561 657 741 729 587
        10 4
        2 7
        3 2
        7 9
        8 4
        5 0
        6 1
        -1 -1
    """

sys.stdin = io.StringIO(q.rstrip())

# ---------------------------------------------------

MAX_ROW = MAX_COL = 11
DR = (0, 1, 1, 1, 0, -1, -1, -1)    # delta row
DC = (1, 1, 0, -1, -1, -1, 0, 1)    # delta col

while True:
    try:
        graph = [tuple(map(int, input().split())) for _ in range(MAX_ROW)]
    except EOFError:
        break

    water = set()
    c, r = map(int, input().split())
    while not (c == r == -1):
        if (r, c) not in water:
            water.add((r, c))
            next_coordinate = [(r + DR[i], c + DC[i]) for i in range(8) if 0 <= r + DR[i] < MAX_ROW and 0 <= c + DC[i] < MAX_COL]
            _, coordinate = min(enumerate(next_coordinate), key=lambda x: (graph[x[1][0]][x[1][1]], x[0]))
            nr, nc = coordinate
            if graph[nr][nc] < graph[r][c]:
                r, c = nr, nc
                continue
        c, r = map(int, input().split())

    print('\n'.join(''.join('.*'[(r, c) in water] for c in range(MAX_COL)) for r in range(MAX_ROW)))
