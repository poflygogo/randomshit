def flip(arr: list) -> list:
    """
    翻轉就是把列反著排序
    """
    return arr[::-1]


def rotate(arr: list) -> list:
    """
    二維矩陣逆時針旋轉90度
    """
    rows, cols = len(arr), len(arr[0])
    result = []
    for col in range(cols - 1, -1, -1):
        new = []
        for row in range(rows):
            new.append(arr[row][col])
        result.append(new)
    return result


data = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
operate = list(map(int, input().split()))
operate.reverse()
for op in operate:
    if op:
        data = flip(data)
    else:
        data = rotate(data)

print(len(data), len(data[0]))
for row in data:
    print(*row)
