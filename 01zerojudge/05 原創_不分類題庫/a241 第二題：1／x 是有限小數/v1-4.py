#  -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a241. 第二題：1 / x 是有限小數
# 
# log2(10^8) ≈ 26
# log2(10^8) ≈ 11 


def mainloop():
    def binary_search(n: int) -> int:
        lft, rgt = 0, len(data) - 1
        while lft < rgt:
            mid = (lft + rgt) // 2
            if data[mid] == n:
                return mid
            if data[mid] > n:
                rgt = mid
            else:
                lft = mid + 1
        return lft - 1

    data = [(2 ** i) * (5 ** j) for i in range(26) for j in range(11)]
    data = [i for i in data if 1 < i < 100000000]
    data.sort()
    for _ in range(int(input())):
        n = int(input())
        print(len(data[:binary_search(n) + 1]))


mainloop()
