# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1233. Remove Sub-Folders from the Filesystem


from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        curr = None
        for item in folder:
            if curr is None or not item.startswith(curr):
                curr = item + '/'
                result.append(item)
        return result



if __name__ == '__main__':
    test = [(["/a/b/c","/a/b/ca","/a/b/d"], ["/a/b/c","/a/b/ca","/a/b/d"])]
    s = Solution()
    for i, j in test:
        print('res:', s.removeSubfolders(i))
        print('ans:', j)
