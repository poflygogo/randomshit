# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a240. 第一題：1 / 17 小數第 n 位
# 
# 題目的 n 給的非常巨大，用暴力解是不理智的
# 1/17 是循環小數，循環結為 0588235294117647 共 16 位數字
# 只需要判斷小數點第 n 位包含幾個循環節，並在循環節的哪個位置結束即可


def mainloop():
    recurring_period = (0, 5, 8, 8, 2, 3, 5, 2, 9, 4, 1, 1, 7, 6, 4, 7)
    for _ in range(int(input())):
        a, b = divmod(int(input()), 16)
        print(recurring_period[b - 1], sum(recurring_period) * a + sum(recurring_period[:b]))


mainloop()
