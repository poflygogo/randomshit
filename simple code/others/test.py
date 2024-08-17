"""
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 1]]

給定一個矩陣, 求被標記為1的區塊有幾個?
上下左右相鄰的1被視為是同一個區塊
"""
def check_blocks(matrix:list):
    matrix = matrix.copy()
    length = len(matrix)

    for row in range(length):
        for column in range(length):
            pass