class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        傳入一個陣列 num 和要移除的元素 val
        並返回該陣列
        """
        while val in nums:
            nums.remove(val)
        return len(nums)