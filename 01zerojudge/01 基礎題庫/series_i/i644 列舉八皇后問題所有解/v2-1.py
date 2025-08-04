# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i644. 列舉八皇后問題所有解

def _eight_queen_puzzle_impl(n: int, path: list, diag1: list, diag2: list, horizon: list):
    if len(path) == n:
        yield ''.join(str(i + 1) for i in path)
        return
    
    row = len(path) - 1
    for col in range(n):
        if not horizon[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            horizon[col] = True
            diag1[row + col] = True
            diag2[row - col + n - 1] = True
            path.append(col)

            yield from _eight_queen_puzzle_impl(n, path, diag1, diag2, horizon)

            horizon[col] = False
            diag1[row + col] = False
            diag2[row - col + n - 1] = False
            path.pop()


def eight_queen_puzzle(size: int):
    diag1 = [False] * (2 * size - 1)
    diag2 = [False] * (2 * size - 1)
    horizon = [False] * size

    path = []
    yield from _eight_queen_puzzle_impl(size, path, diag1, diag2, horizon)


def main():
    cnt = 1
    for item in eight_queen_puzzle(8):
        print(f"{cnt}: {item}")
        cnt += 1


if __name__ == "__main__":
    main()
