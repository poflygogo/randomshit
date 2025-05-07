# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d512. 創造數字


def create_number(nums: set):
    def dfs(nums, path):
        if not nums:
            return
        result.add(sum(path))
        for num in nums:
            dfs(nums - {num}, path + [num])

    result = set()
    dfs(nums, [])
    return len(result)


def main():
    while True:
        try:
            n = int(input())
            nums = set(map(int, input().split()))
            print(create_number(nums))
        except EOFError:
            break


if __name__ == '__main__':
    main()
