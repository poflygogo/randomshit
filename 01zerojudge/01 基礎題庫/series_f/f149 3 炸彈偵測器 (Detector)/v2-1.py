# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f149. 3. 炸彈偵測器 (Detector)
# 2020-06 TOI 練習賽 新手組


def test():
    for i in range(1, 6):
        with open(f'./test_case/f149_{i:02d}.in') as f:
            rows, cols = map(int, f.readline().rstrip().split())
            data = [f.readline().rstrip().split() for _ in range(rows)]
            detect, undetect = detector(rows, cols, data)
        with open(f'./test_case/f149_{i:02d}.out') as f:
            a, b = map(int, f.readline().rstrip().split())
            if (a, b) == (detect, undetect):
                print(f'{i:02d} AC',
                      end='\n\n')
            else:
                print(f'{i:02d} WA',
                      f'my ans: {detect:2d} {undetect:2d}',
                      f'gd ans: {a:2d} {b:2d}',
                      sep='\n',
                      end='\n\n')


def detector(rows: int, cols: int, data: list) -> tuple:
    """ 1. 遍歷一次　data，把讀到的炸彈資訊和可用的偵測器都記錄起來。
        2. 遍歷一次 all_bombs，檢視有多少炸彈被偵測到
    """
    all_bombs = set()   # 紀錄所有炸彈的位置
    detectors = set()   # 紀錄有效的偵測器

    for row in range(rows):
        for col in range(cols):
            if data[row][col] == '1':
                all_bombs.add((row, col))
            elif data[row][col] == '5' and \
                    all(data[r][c] != '5'
                        for r in range(max(0, row - 1), min(rows, row + 2))
                        for c in range(max(0, col - 1), min(cols, col + 2))
                        if (r, c) != (row, col)):
                detectors.add((row, col))

    a = sum(any((r, c) in detectors
                for r in range(max(0, row - 1), min(rows, row + 2))
                for c in range(max(0, col - 1), min(cols, col + 2)))
            for row, col in all_bombs)
    return a, len(all_bombs) - a


def main():
    rows, cols = map(int, input().split())
    data = [input().split() for _ in range(rows)]
    print(*detector(rows, cols, data))


if __name__ == '__main__':
    main()
