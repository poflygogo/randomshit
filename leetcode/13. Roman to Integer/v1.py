class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rome_dict = {
        'I': 1,'V': 5,'X': 10,'L': 50,
        'C': 100,'D': 500,'M': 1000}
        outnum = rome_dict[s[0]]
        for index in range(1,len(s)):
            if rome_dict[s[index]] <= rome_dict[s[index-1]]:
                outnum += rome_dict[s[index]]
            else:
                outnum = outnum - rome_dict[s[index-1]] * 2 + rome_dict[s[index]]
        return outnum
