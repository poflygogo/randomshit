class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result = []
        for command in operations:
            match command:
                case '+':
                    result.append(result[-1] + result[-2])
                case 'D':
                    result.append(result[-1] * 2)
                case 'C':
                    del result[-1]
                case _:
                    result.append(int(command))
        return sum(result)