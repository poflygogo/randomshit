class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lft, rgt = 0, len(nums)
        while lft < rgt:
            mid = (lft + rgt) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                rgt = mid
            else:
                lft = mid + 1
        return -1