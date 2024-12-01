class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        match numRows:
            case 0:
                return []
            case 1:
                return [[1]]
            case 2:
                return [[1], [1, 1]]
        pascal = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            pascal.append([1] * i)
            for j in range(1, i - 1):
                pascal[-1][j] = sum(pascal[-2][j - 1:j + 1])
        return pascal