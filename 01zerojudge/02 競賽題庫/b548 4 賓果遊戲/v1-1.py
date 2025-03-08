# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b548. 4.賓果遊戲
# 102學年度北基區北三區資訊學科能力競賽


def best_choice(data: list, nums: dict) -> int:
    score = {i: 0 for i in range(1, 26)}
    for i in nums:
        r, c = nums[i]
        if data[r][c] is not None:
            score[i] = count_score(data, r, c)
    return max(range(1, 26), key=lambda x: (score[x], -x))


def count_score(data: list, row: int, col: int) -> int:
    result = 0
    if all(i is None for i in data[row] if i != data[row][col]):
        result += 1
    if all(data[i][col] is None for i in range(5) if i != row):
        result += 1
    if row == col and all(data[i][i] is None for i in range(5) if i != row):
        result += 1
    if row + col == 4 and all(data[i][4-i] is None for i in range(5) if i != row):
        result += 1
    return result


def get_nums_locations(data):
    result = {i: None for i in range(1, 26)}
    for i in range(5):
        for j in range(5):
            result[data[i][j]] = (i, j)
    return result


def main():
    data = [list(map(int, input().split())) for _ in range(5)]
    nums = get_nums_locations(data)

    n = int(input())
    while n != -1:
        r, c = nums[n]
        data[r][c] = None
        n = int(input())    
    print(best_choice(data, nums))


if __name__ == '__main__':
    main()
