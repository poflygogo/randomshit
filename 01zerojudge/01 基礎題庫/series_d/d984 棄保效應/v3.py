while True:
    # 無限循環至EOF為止
    try:
        a, b, c = map(int, input().split())
    except EOFError:
        break

    # 將候選人資料做成嵌套list, 然後根據每組數據的第二的數據做排序
    candidate = [(a,'A'), (b,'B'), (c,'C')]
    candidate.sort()

    # 邏輯判斷
    if candidate[0][0] + candidate[1][0] > candidate[2][0]:
        print(candidate[1][1])
    else:
        print(candidate[2][1])