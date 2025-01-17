class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lft, rgt = 0, x
        while lft < rgt:
            mid = (lft + rgt) // 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp < x:
                lft = mid + 1
            else:
                rgt = mid
        return lft - 1
