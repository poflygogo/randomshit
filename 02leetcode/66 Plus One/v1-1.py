class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for idx in range(len(digits) - 1, -1 , -1):
            if digits[idx] > 9:
                digits[idx] %= 10
                if idx > 0:
                    digits[idx - 1] += 1
                else:
                    return [1] + digits
            else:
                return digits
