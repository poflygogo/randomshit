# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a270. 爬樓梯有益身心健康


def climb_stairs(break_time: int, stair_data: list, class_data: list) -> bool:
    for i in range(1, len(class_data)):
        low, high = sorted([class_data[i-1], class_data[i]])
        if sum(stair_data[j] for j in range(low - 1, high - 1)) > break_time:
            return False
    return True


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
