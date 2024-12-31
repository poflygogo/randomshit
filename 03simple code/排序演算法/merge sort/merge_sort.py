# -*- encoding: utf-8 -*-
# python 3.12


class SortAlgorithm:
    def merge_sort(self, nums: list[int]) -> list[int]:
        if type(nums) != list:
            raise TypeError(f"{nums} is not list[int].")
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        lft = self.merge_sort(nums[:mid])
        rgt = self.merge_sort(nums[mid:])
        return self.merge(lft, rgt)
    
    @staticmethod
    def merge(nums1, nums2) -> list[int]:
        idx = 0
        while idx < len(nums1) and nums2:
            if nums2[0] < nums1[idx]:
                nums1.insert(idx, nums2.pop(0))
            idx += 1
        if nums2:
            nums1.extend(nums2)
        return nums1


if __name__ == '__main__':
    my_list = [9, 8, 7, 6, 3, 4, 5, 2, 3, 1]
    s = SortAlgorithm()
    print(s.merge_sort(my_list))
