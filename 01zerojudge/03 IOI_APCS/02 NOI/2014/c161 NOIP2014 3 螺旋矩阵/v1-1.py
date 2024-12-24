# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c161. NOIP2014 3.螺旋矩阵
# NOIP 2014 普及組 第三題
# 
# 題目的 n 相當巨大 (1 ≤ n ≤ 30,000)
# 所以把該螺旋矩陣做出來是不理智的，應尋找 O(n) 解


def main():
    n, i, j = map(int, input().split())

    # 計算 (i, j) 在第幾層
    # 說明: 計算 (i, j) 與四條邊界的距離
    layer = min(i - 1, j - 1, n - i, n - j)

    # 計算第 layer 層的起始值
    start_value = 1 + 4 * layer * (n - layer)

    # 第 layer 層的大小(元素總數)
    size = n - 2 * layer

    if i == layer + 1:        # 上邊界
        print(start_value + j - (layer + 1))
    elif j == n - layer:      # 右邊界
        print(start_value + (size - 1) + (i - (layer + 1)))
    elif i == n - layer:      # 下邊界
        print(start_value + 2 * (size - 1) + ((n - layer) - j))
    else: # if j == layer + 1 # 左邊界
        print(start_value + 3 * (size - 1) + ((n - layer) - i))


if __name__ == '__main__':
    main()
