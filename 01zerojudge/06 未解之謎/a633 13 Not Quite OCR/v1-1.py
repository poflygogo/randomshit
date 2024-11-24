# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a633. 13. Not Quite OCR
# HP CodeWars 2007


# 建立數字對照表，注意字典的 key 必須是可哈希的，不能使用可變物件作為 key，如 list, dict, set
num_key = {
    (0, 0, 0, 0, 0, 1, 0, 0, 1): 1, (0, 1, 0, 0, 1, 1, 1, 1, 0): 2, (0, 1, 0, 0, 1, 1, 0, 1, 1): 3,
    (0, 0, 0, 1, 1, 1, 0, 0, 1): 4, (0, 1, 0, 1, 1, 0, 0, 1, 1): 5, (0, 1, 0, 1, 1, 0, 1, 1, 1): 6,
    (0, 1, 0, 0, 0, 1, 0, 0, 1): 7, (0, 1, 0, 1, 1, 1, 1, 1, 1): 8, (0, 1, 0, 1, 1, 1, 0, 1, 1): 9,
    (0, 1, 0, 1, 0 ,1, 1, 1, 1): 0
}

for _ in range(int(input())):
    # 讀取資料的同時並將資料轉譯成 1 與 0 構成的陣列
    data = [list(map(lambda x: 1 if ord(x) != 32 else 0, input())) for _ in range(3)]

    # 將讀進來的資料進行切割、每個數字用一維陣列表達
    num_encode = []
    while any(data):
        temp = []
        for i in range(3):
            temp.extend(data[i][:3])
        num_encode.append(tuple(temp))
        data = [i[3:] for i in data]

    # 解碼，將得到的資訊轉換成 1-9 的數字
    num_decode = []
    for code in num_encode:
        if code in num_key:
            num_decode.append(num_key[code])
        else:
            # TODO: 若資料有損的處理方式。要窮舉可能的值嗎?
            num_decode.append(None)

    # TODO: 要滿足什麼條件才會輸出 ambiguous?
    if sum((9 - i) * j for i, j in enumerate(num_decode)) % 11 == 0:
        print(''.join(str(i) for i in num_decode))
    
    else:
        print('failure')
