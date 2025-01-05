# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a981. 求和問題


def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    combination_sum(nums, m, [])



def combination_sum(iterable: list, target: int, path: list, start_idx: int=0, curr_sum: int=0):
    if target == curr_sum:
        print(*path)
        return
    if target < curr_sum:
        return
    for i in range(start_idx, len(iterable)):
        path.append(iterable[i])
        combination_sum(
            iterable,
            target,
            path,
            i + 1,
            curr_sum + iterable[i]
        )
        path.pop()

if __name__ == '__main__':
    main()
    # line1 = '10 100'
    # line2 = '10 20 40 30 50 80 60 70 5 15'
    # n, m = map(int, line1.split())
    # nums = list(map(int, line2.split()))
    # nums.sort()
    # combination_sum(nums, m, [])
