class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = []
        for i in range(1, numRows + 1):
            pascal.append([1] * i)
            for j in range(1, i - 1):
                pascal[-1][j] = sum(pascal[-2][j - 1:j + 1])
        return pascal