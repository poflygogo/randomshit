from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row, temp = [1], None
        for i in range(1, rowIndex + 1):
            temp = [1] * (i + 1)
            for j in range(1, i):
                temp[j] = sum(row[j-1:j+1])
            row = temp
        return temp