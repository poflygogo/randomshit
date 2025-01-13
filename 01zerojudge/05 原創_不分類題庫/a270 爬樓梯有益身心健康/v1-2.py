# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a270. 爬樓梯有益身心健康


def climb_stairs(break_time: int, stair_data: list, class_data: list) -> bool:
    stair_data = prefix_sum(stair_data)
    for i in range(1, len(class_data)):
        if abs(stair_data[class_data[i] - 1] - stair_data[class_data[i - 1] - 1]) > break_time:
            return False
    return True


def prefix_sum(stair_data: list) -> list:
    prefix_sum = [0] * (len(stair_data) + 1)
    for i, j in enumerate(stair_data):
        prefix_sum[i + 1] = prefix_sum[i] + j
    return prefix_sum


def main():
    while True:
        try:
            break_time = int(input())
            stair_data = list(map(int, input().split()))
            class_data = list(map(int, input().split()))
        except EOFError:
            break
        if climb_stairs(break_time, stair_data, class_data):
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    main()
