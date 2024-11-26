class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lft, rgt = 0, len(nums)
        while lft < rgt:
            mid = (lft + rgt) // 2
            if nums[mid] < target:
                lft = mid + 1
            else:
                rgt = mid
        return lft
