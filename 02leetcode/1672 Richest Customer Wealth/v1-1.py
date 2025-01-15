# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1672. Richest Customer Wealth


from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)
