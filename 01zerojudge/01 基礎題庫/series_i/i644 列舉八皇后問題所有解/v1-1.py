# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i644. 列舉八皇后問題所有解


def is_valid(arr: list, target: int):
    curr = len(arr)
    for i in range(curr):
        diff = curr - i
        if arr[i] in (target - diff, target, target + diff):
            return False
    return True


def eight_queen_puzzle(path: list = None, n: int = 8):
    if path is None:
        path = []
    if len(path) == n:
        yield "".join(str(i + 1) for i in path)
        return
    for i in range(n):
        if is_valid(path, i):
            path.append(i)
            yield from eight_queen_puzzle(path, n)
            path.pop()


def main():
    cnt = 1
    for i in eight_queen_puzzle():
        print(f"{cnt}: {i}")
        cnt += 1


if __name__ == "__main__":
    main()
