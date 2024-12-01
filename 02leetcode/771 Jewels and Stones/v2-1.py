class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        stones = Counter(stones)
        return sum(stones[i] for i in stones if i in set(jewels))