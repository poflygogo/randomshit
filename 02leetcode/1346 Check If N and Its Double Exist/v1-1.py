# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1346. Check If N and Its Double Exist


from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
            if n * 2 in seen or n / 2 in seen:
                return True
            seen.add(n)
        return False
