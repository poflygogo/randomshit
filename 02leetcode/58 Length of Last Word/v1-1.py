class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().rsplit(' ', 1)[-1])
        