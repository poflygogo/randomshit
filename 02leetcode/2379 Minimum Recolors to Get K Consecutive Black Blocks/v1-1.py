# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 2379. Minimum Recolors to Get K Consecutive Black Blocks


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = len(blocks)
        for i in range(len(blocks) - k + 1):
            result = min(result, blocks[i : i + k].count('W'))
        return result


if __name__ == '__main__':
    test = [("WBBWWBBWBW", 7), ('WBWBBBW', 2), ('BWWWBB', 6)]
    s = Solution()
    for i, j in test:
        print(s.minimumRecolors(i, j))
