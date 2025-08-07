# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 3477. Fruits Into Baskets II


from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        flag = [False] * len(baskets)
        cnt = 0
        for i in fruits:
            for j in range(len(baskets)):
                if flag[j] is False and baskets[j] >= i:
                    flag[j] = True
                    break
            else:
                cnt += 1
        return cnt


if __name__ == "__main__":
    s = Solution()
    assert s.numOfUnplacedFruits([4, 2, 5], [3, 5, 4]) == 1
    print("pass")
