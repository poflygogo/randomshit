class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        lft, top, rgt, sub = 0, 0, len(matrix[0]), len(matrix)
        direct = 0
        result = []
        while len(result) < len(matrix) * len(matrix[0]):
            match direct:
                case 0:
                    result.extend(matrix[top][lft:rgt])
                    top += 1
                case 1:
                    result.extend(matrix[row][rgt - 1] for row in range(top, sub))
                    rgt -= 1
                case 2:
                    result.extend(reversed(matrix[sub - 1][lft:rgt]))
                    sub -= 1
                case 3:
                    result.extend(matrix[row][lft] for row in range(sub - 1, top - 1, -1))
                    lft += 1
            direct = (direct + 1) % 4
        return result
