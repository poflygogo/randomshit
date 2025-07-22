# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e167. 演唱會記行 - 排隊買周邊


direction = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
direction.extend([(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in direction])
direction.remove((0, 0))
seen = set()


def _is_valid(max_row: int, max_col: int, graph: list, row: int, col: int):
    """檢查目標座標是否合法"""
    return (
        (row, col) not in seen  # 避免往回走
        and 0 <= row < max_row  # 避免超出範圍
        and 0 <= col < max_col
        and graph[row][col] == 1  # 確認該位置的確是人
    )


# dfs
def _find_the_tail(max_row: int, max_col: int, graph: list, row: int, col: int):
    """
    args:
        max_row(int): 最大高度
        max_col(int): 最大寬度
        graph(list[int]): 完整地圖資料
        row(int): 當前節點的橫坐標
        col(int): 當前節點的縱坐標
        jump(bool): 紀錄是否需要跳躍
    """
    tail = (row, col)
    seen.add(tail)
    # 邏輯重複，只差在遍歷的節點不同，也許這邊還能再分一個函數出去?
    for i, j in direction:
        r, c = row + i, col + j
        if _is_valid(max_row, max_col, graph, r, c):
            seen.add((r, c))
            tail = _find_the_tail(max_row, max_col, graph, r, c)
            break
    return tail


def find_the_tail(max_row: int, max_col: int, graph: list, row: int, col: int):
    """目的只是用來呼叫 _find_the_tail，刻意分離是因為需要重設 seen，我認為把這段邏輯放這會更清晰"""
    seen.clear()
    return _find_the_tail(max_row, max_col, graph, row, col)


def main():
    n, m = map(int, input().split())
    while not n == m == 0:
        graph = [list(map(int, input().split())) for _ in range(n)]
        x, y = map(int, input().split())
        print(*find_the_tail(n, m, graph, x, y))
        n, m = map(int, input().split())


if __name__ == "__main__":
    main()
