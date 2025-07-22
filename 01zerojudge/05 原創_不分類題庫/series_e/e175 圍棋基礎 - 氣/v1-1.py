# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e175. 圍棋基礎 - 氣


from collections import deque


DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"({self.row}, {self.col})"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Node):
            return NotImplemented
        return self.row == value.row and self.col == value.col
    
    def __hash__(self) -> int:
        return hash((self.row, self.col))


def count_liberties(size: int, board: list, target: Node):
    if board[target.row][target.col] == ".":
        return 0
    cnt = 0
    queue = deque([target])
    seen = {target}
    while queue:
        node = queue.popleft()
        for i, j in DIRECTION:
            next_node = Node(node.row + i, node.col + j)
            if (
                next_node not in seen
                and 0 <= next_node.row < size
                and 0 <= next_node.col < size
            ):
                if board[next_node.row][next_node.col] == board[target.row][target.col]:
                    queue.append(next_node)
                elif board[next_node.row][next_node.col] == ".":
                    cnt += 1
                seen.add(next_node)
    return cnt


def main():
    n = int(input())
    while n:
        board = [input() for _ in range(n)]
        for _ in range(int(input())):
            x, y = map(int, input().split())
            print(count_liberties(n, board, Node(n - y, x - 1)))
        n = int(input())


main()
