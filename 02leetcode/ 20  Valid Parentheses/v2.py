class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        maping = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in maping.keys():
                if not stack or stack.pop() != maping[i]:
                    return False
            elif i in maping.values():
                stack.append(i)
        else:
            return not stack