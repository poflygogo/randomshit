# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00256 Quirksome Squares
# ZeroJudge d182

# 考慮數字最大為 1e9-1 ，將該數字分割成兩半後相加，應介於 0 - 9999 之間
# 故開一個陣列，用來紀錄任意數字分割成兩半、相加、取平方的結果
quirk_number = [i * i for i in range(10000)]

while True:
    try:
        n = int(input())

    except EOFError:
        exit()

    else:
        for i in range(len(quirk_number)):
            # 當數值超出範圍就退出循環
            if quirk_number[i] >= pow(10, n):
                break

            # 將數字分成左右兩半，分別以 lft 和 rgt 表示
            lft, rgt = quirk_number[i] // pow(10, n // 2), quirk_number[i] % pow(10, n // 2)
            if pow(lft + rgt, 2) == quirk_number[i]:
                print(str(quirk_number[i]).zfill(n))
