def ss(data):
    length = len(data)
    for i in range(length - 1):
        m = i
        for j in range(i + 1, length):
            if data[j] < data[m]:
                m = j
        if i != m:
            data[i], data[m] = data[m], data[i]     # 交換
    return data

if __name__ == '__main__':
    print(
        ss([9, 7, 4, 2, 8, 4, 6, 1])
    )