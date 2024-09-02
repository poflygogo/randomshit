class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()

        for idx, item in enumerate(strs[0]):
            for i in strs[1:]:
                if item != i[idx]:
                    return strs[0][:idx]
        else:
            return strs[0]