while True:
    # 無限循環至EOF為止
    try:
        a, b, c = map(int, input().split())
    except EOFError:
        break

    # 將候選人資料做成嵌套list, 然後根據每組數據的第二的數據做排序
    candidate = [('A', a), ('B', b), ('C', c)]
    candidate.sort(key= lambda n: n[1])

    # 邏輯判斷
    if candidate[0][1] + candidate[1][1] > candidate[2][1]:
        print(candidate[1][0])
    else:
        print(candidate[2][0])
