# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q182. 2. 字串操作
# 2025-01 APCS


from sys import stdin


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
    s = StringManipulate(stdin.readline().rstrip())
    k = int(stdin.readline().rstrip())
    commands = stdin.read().splitlines()
    idx = 0
    while idx < k:
        if commands[idx] == '0':
            if idx < k - 1 and commands[idx] == commands[idx + 1]:
                idx += 1
            else:
                s.swap()
        elif commands[idx] == '1':
            if idx == 0 or commands[idx - 1] != '1':
                s.sort()
        else:
            s.merge()
        idx += 1
    print(''.join(s.ans))


if __name__ == '__main__':
    main()
