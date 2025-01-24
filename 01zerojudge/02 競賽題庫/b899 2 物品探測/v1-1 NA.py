# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b899. 2. 物品探測
# 2016 高雄市資訊學科能力複賽


def sort_the_points(data):
    def calc(i):
        return (data[i[0]][0] - data[i[1]][0]) ** 2 + (data[i[0]][1] - data[i[1]][1]) ** 2
    a, c = max(
        ((0, 1), (0, 2), (1, 2)),
        key=calc
    )
    b = (a + c) % 3
    return data[a], data[b], data[c]


def main():
    data = [tuple(map(int, input().split())) for _ in range(3)]
    a, b, c = sort_the_points(data)
    print(c[0] + a[0] - b[0], c[1] + a[1] - b[1])


if __name__ == '__main__':
    main()
