class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[False] * n for _ in range(n)]
        lft, rgt, top, sub = 0, n - 1, 0, n - 1
        num = iter(range(1, n * n + 1))
        while lft <= rgt and top <= sub:
            for col in range(lft, rgt + 1):
                matrix[top][col] = next(num)
            top += 1

            for row in range(top, sub + 1):
                matrix[row][rgt] = next(num)
            rgt -= 1

            for col in range(rgt, lft - 1, -1):
                matrix[sub][col] = next(num)
            sub -= 1

            for row in range(sub, top - 1, -1):
                matrix[row][col] = next(num)
            lft += 1
        return matrix
