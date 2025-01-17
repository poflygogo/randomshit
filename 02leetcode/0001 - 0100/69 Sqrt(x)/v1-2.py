class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        lft, rgt = 1, x
        while lft <= rgt:
            mid = (lft + rgt) // 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp < x:
                lft = mid + 1
            else:
                rgt = mid - 1
        return rgt
