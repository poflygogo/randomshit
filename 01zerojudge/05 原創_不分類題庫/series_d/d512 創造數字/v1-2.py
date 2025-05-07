# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d512. 創造數字


def create_number(length: int, nums: tuple):
    def dfs(path: list, start: int, end: int):
        if path:
            result.add(sum(path))
        if start == end:
            return
        for i in range(start, end):
            path.append(nums[i])
            dfs(path, i + 1, end)
            path.pop()

    result = set()
    dfs([], 0, length)
    return len(result)


def main():
    while True:
        try:
            n = int(input())
            nums = tuple(map(int, input().split()))
            print(create_number(n, nums))
        except EOFError:
            break


if __name__ == '__main__':
    main()
