# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q182. 2. 字串操作
# 2025-01 APCS


class StringManipulate:
    def __init__(self, s: str):
        self.ans = list(s)
    
    def grouper(self, n: int=2):
        iterators = [iter(self.ans)] * n
        return zip(*iterators)
    
    def swap(self):
        temp = self.grouper()
        self.ans = [item for line in [[j, i] for i, j in temp] for item in line]
    
    def sort(self):
        temp = self.grouper()
        temp = [sorted(i) for i in temp]
        self.ans = [j for i in temp for j in i]

    def merge(self):
        self.ans = [self.ans[j] for i in zip(range(len(self.ans) // 2), range(len(self.ans) // 2, len(self.ans))) for j in i]


def main():
    s = StringManipulate(input().rstrip())
    for _ in range(int(input())):
        command = input().rstrip()
        if command == '0':
            s.swap()
        elif command == '1':
            s.sort()
        else:
            s.merge()
    print(''.join(s.ans))


if __name__ == '__main__':
    main()
