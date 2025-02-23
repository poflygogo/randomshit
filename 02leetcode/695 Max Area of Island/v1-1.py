# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 695. Max Area of Island


from typing import List, Set


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == 1:
                    result = max(result, self.bfs(seen, grid, r, c))
        return result

    def bfs(self, seen: Set, grid: List[List[int]], r: int, c: int):
        queue = [(r, c)]
        temp = set(queue)
        while queue:
            r, c = queue.pop(0)
            for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (i, j) not in temp and 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    temp.add((i, j))
                    queue.append((i, j))
        seen.update(temp)
        return len(temp)


if __name__ == '__main__':
    s = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(s.maxAreaOfIsland(grid))
