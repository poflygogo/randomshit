class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        idx = 0
        while idx < len(nums1) and nums2:
            if nums2[0] < nums1[idx]:
                nums1.insert(idx, nums2.pop(0))
            idx += 1
        if nums2:
            nums1.extend(nums2)