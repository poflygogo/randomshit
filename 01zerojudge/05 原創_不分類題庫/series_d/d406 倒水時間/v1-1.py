# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d406. 倒水時間


from sys import stdin

scan = stdin.readline

test_case = 1
for s in stdin:
    s = bool(s.rstrip() == '1')
    max_row, max_col = map(int, scan().rstrip().split())
    graph = [tuple(map(int, scan().rstrip().split())) for _ in range(max_row)]
    result = [[0] * max_col for _ in range(max_row)]
    
    queue = [(0, graph[0].index(1), 1)]
    while queue:
        r, c, depth = queue.pop(0)
        result[r][c] = depth
        depth += 1
        for i, j in [(r, c + 1), (r, c - 1), (r + 1, c)] + [(r - 1, c)] * s:
            if 0 <= i < max_row and 0 <= j < max_col and graph[i][j] == 1 and result[i][j] == 0:
                queue.append((i, j, depth))

    print(
        f'Case {test_case}:',
        '\n'.join(' '.join(map(str, i)) for i in result),
        sep='\n'
    )
    test_case += 1
