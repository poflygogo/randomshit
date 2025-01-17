class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 原地修改 nums，並輸出有幾個不同的數字
        idx = 0
        counter = {}
        while idx < len(nums) and nums[idx] != None:
            if counter.get(nums[idx], True):
                counter[nums[idx]] = False
                idx += 1
            else:
                del nums[idx]
                nums.append(None)
        return idx
