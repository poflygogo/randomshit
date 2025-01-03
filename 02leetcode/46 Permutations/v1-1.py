# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 46. Permutations


from typing import List, Set


class Solution:
    def __init__(self):
        self.result = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutation(nums, set(), [])
        return self.result

    def permutation(self, iterable: List[int], visit: Set[int], perm: List[int]):
        if len(iterable) == len(visit):
            self.result.append(perm.copy())
            return
        for item in iterable:
            if item not in visit:
                perm.append(item)
                visit.add(item)
                self.permutation(iterable, visit, perm)
                perm.pop()
                visit.remove(item)


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
