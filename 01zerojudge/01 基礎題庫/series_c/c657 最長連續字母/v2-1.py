while True:
    try:
        data = input()
    except EOFError:
        break

    group = []          # 保存所有子序列的字母, 長度
    char = data[0]      # 保存子序列的字母
    start = 0           # 保存子序列的起始位置
    for i in range(1, len(data)):
        if data[i] != char:
            group.append((char, i - start))
            start = i
            char = data[i]
    
    # 邊緣處理，循環到最後時，最後一個子序列資料並不會被添加到group中，要另外補上
    else:
        group.append((char, len(data) - start))
    
    print(*max(group, key=lambda x: x[1]))
