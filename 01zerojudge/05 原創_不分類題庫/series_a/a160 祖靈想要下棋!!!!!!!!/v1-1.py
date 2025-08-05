# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a160. 祖靈想要下棋!!!!!!!!


def queen(size: int):
    diag1 = [True] * (2 * size - 1)
    diag2 = [True] * (2 * size - 1)
    horizon = [True] * size

    path = []

    def _impl():
        if len(path) == size:
            yield path
            return

        row = len(path)
        for col in range(size):
            if horizon[col] and diag1[row + col] and diag2[row - col + size - 1]:
                horizon[col] = False
                diag1[row + col] = False
                diag2[row - col + size - 1] = False
                path.append(col)

                yield from _impl()

                horizon[col] = True
                diag1[row + col] = True
                diag2[row - col + size - 1] = True
                path.pop()

    yield from _impl()


def print_board(size: int, arr: list, blank: str = "x", queen: str = "Q"):
    result = [[blank] * size for _ in range(size)]
    for row, col in enumerate(arr):
        result[row][col] = queen
    print("\n".join("".join(i) for i in result), end="\n\n")


def main():
    is_first_line = True
    n = int(input())
    while n:
        if not is_first_line:
            print()
        cnt = 0
        for item in queen(n):
            print_board(n, item)
            cnt += 1
        print(f"{cnt}")
        n = int(input())
        is_first_line = False


if __name__ == "__main__":
    main()
