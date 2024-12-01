class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(i in set(jewels) for i in stones)