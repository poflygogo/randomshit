# 建立候選人資料，用string保存
output = 'ABC'

while True:
    # 無限循環至EOF為止
    try:
        candidate = [(index,value) for index, value in enumerate(map(int, input().split()))]
    except EOFError:
        break

    candidate.sort(key= lambda n: n[1])

    # 邏輯判斷
    if candidate[0][1] + candidate[1][1] > candidate[2][1]:
        print(output[candidate[1][0]])
    else:
        print(output[candidate[2][0]])