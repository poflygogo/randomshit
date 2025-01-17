class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            elif stack:
                item = stack.pop()
                if (i == ')' and item == '(') or (i == ']' and item == '[') or (i == '}' and item == '{'):
                    continue
                else:
                    return False
            else:
                return  False

        else:
            if stack:
                return False
            else:
                return True