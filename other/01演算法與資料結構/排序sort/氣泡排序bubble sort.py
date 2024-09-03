def bs(data):
    length = len(data)
    for i in range(length - 1, 0, -1):      # 每次要遍歷的範圍越來越小
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]     # 交換
    return data

if __name__ == '__main__':
    print(
        bs([9, 7, 4, 2, 8, 4, 6, 1])
    )