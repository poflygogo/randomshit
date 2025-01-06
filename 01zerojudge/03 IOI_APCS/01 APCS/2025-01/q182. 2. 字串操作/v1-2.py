# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q182. 2. 字串操作
# 2025-01 APCS


class StringManipulate:
    def __init__(self, s: str):
        self.ans = list(s)
    
    def swap(self):
        for i in range(0, len(self.ans), 2):
            self.ans[i], self.ans[i + 1] = self.ans[i + 1], self.ans[i]
    
    def sort(self):
        for i in range(0, len(self.ans), 2):
            self.ans[i], self.ans[i + 1] = sorted(self.ans[i:i + 2])

    def merge(self):
        mid = len(self.ans) // 2
        self.ans = [self.ans[j] for i in range(mid) for j in (i, i + mid)]


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
