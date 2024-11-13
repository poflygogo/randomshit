from sys import stdin


for line in stdin:
    line = [int(i) for i in line.rstrip().split()]
    if line == [0, 0, 0, 0]:
        exit()

    print(
        1080 +                                                  # 360 * (2 + 1)
        9 * (line[0] - line[1] + 40 * (line[1] > line[0]) +     # 順時鐘轉直到到達第 1 個號碼
             line[2] - line[1] + 40 * (line[1] > line[2]) +     # 逆時鐘轉直到到達第 2 個號碼
             line[2] - line[3] + 40 * (line[3] > line[2]))      # 順時鐘轉直到到達第 3 個號碼
    )
