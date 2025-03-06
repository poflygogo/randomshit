# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b545. 1.蟲蟲鑽洞問題


def worm(max_row: int, max_col: int, graph: list) -> list:
    curr_r, curr_c = find_first_hole(max_row, max_col, graph)
    last_r, last_c = curr_r, curr_c
    vertex = [(curr_c, curr_r)]
    seen = {(curr_r, curr_c)}
    while True:
        for i, j in ((curr_r + 1, curr_c), (curr_r - 1, curr_c), (curr_r, curr_c - 1), (curr_r, curr_c + 1)):
            if ((i, j) not in seen) and (0 <= i < max_row) and (0 <= j < max_col) and (graph[i][j] == '*'):
                seen.add((i, j))
                next_r, next_c = i, j
                break
        else:
            vertex.append((curr_c, curr_r))
            break

        if (not last_r == curr_r == next_r) and (not last_c == curr_c == next_c):
            vertex.append((curr_c, curr_r))
        last_r, last_c, curr_r, curr_c = curr_r, curr_c, next_r, next_c
    
    if vertex[-1][0] < vertex[0][0] or (vertex[-1][0] == vertex[0][0] and vertex[-1][1] < vertex[0][1]):
        return vertex[::-1]
    else:
        return vertex


def find_first_hole(row: int, col: int, graph: list) -> tuple:
    c = 0
    for r in range(row):
        if (graph[r][c] == '*' and 
            sum(bool(0 <= i < row and graph[i][j] == '*') for i, j in ((r + 1, c), (r - 1, c), (r, c + 1))) == 1):  
            return r, c
    for c in range(1, col):
        for r in (0, row - 1):
            if (graph[r][c] == '*' and
                sum(bool(0 <= i < row and 0 <= j < col and graph[i][j] == '*') for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))) == 1):
                return r, c
    c = col - 1
    for r in range(1, row - 1):
        if (graph[r][c] == '*' and sum(bool(graph[i][j] == '*') for i, j in ((r + 1, c), (r - 1, c), (r, c - 1))) == 1):
            return r, c


def main():
    col, row = map(int, input().split())
    graph = [input() for _ in range(row)]
    result = worm(row, col, graph)
    print('\n'.join(f'{i + 1} {j + 1}' for i, j in result))


if __name__ == '__main__':
    main()
