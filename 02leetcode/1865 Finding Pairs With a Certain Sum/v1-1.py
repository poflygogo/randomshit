# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1865. Finding Pairs With a Certain Sum


from typing import List
import collections


class FindSumPairs:
    
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums1_counter = collections.Counter(nums1)
        self.nums2_counter = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_counter[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(
            self.nums2_counter[tot - i] * j for i, j in self.nums1_counter.items()
        )


if __name__ == "__main__":
    test_comm = [
        "FindSumPairs",
        "count",
        "add",
        "count",
        "count",
        "add",
        "add",
        "count",
    ]
    test_val = [
        [[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]],
        [7],
        [3, 2],
        [8],
        [4],
        [0, 1],
        [1, 1],
        [7],
    ]

    s = FindSumPairs(*test_val[0])
    for i in range(1, len(test_comm)):
        match test_comm[i]:
            case "add":
                s.add(*test_val[i])
                print("null")
            case "count":
                print(s.count(test_val[i][0]))
