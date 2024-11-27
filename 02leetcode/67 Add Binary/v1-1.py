class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(sum(map(lambda x: int(x, 2), (a, b))))[2:]
