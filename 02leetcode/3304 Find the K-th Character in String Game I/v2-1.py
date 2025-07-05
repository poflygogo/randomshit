# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 3304. Find the K-th Character in String Game I


class Solution:
    def kthCharacter(self, k: int) -> str:
        # 注意到:
        # 每次計算都會添加二進制表示的 k-1 的 1 的數量
        # 所以只需要計算 k-1 轉換成二進制表達後有幾個 1 就好
        return chr(ord("a") + (k - 1).bit_count())


if __name__ == "__main__":
    test = [5, 10]
    s = Solution()
    for i in test:
        print(s.kthCharacter(i))
