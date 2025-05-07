# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d452. 二、直線最小距離和
# 98學年度板橋高中校內資訊學科能力競賽


def min_distance(length: int, points: list) -> int:
    if length < 2:
        return 0
    points.sort()
    mid = length // 2
    if length % 2 != 0:
        return sum(abs(points[i] - points[mid]) for i in range(length))
    return min(
        sum(abs(points[i] - points[mid]) for i in range(length)),
        sum(abs(points[i] - points[mid - 1]) for i in range(length))
    )


def main():
    for _ in range(int(input())):
        length, *points = map(int, input().split())
        print(min_distance(length, points))


if __name__ == '__main__':
    main()
