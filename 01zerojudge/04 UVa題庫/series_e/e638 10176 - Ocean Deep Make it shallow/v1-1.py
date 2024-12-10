# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10176 Ocean Deep! Make it shallow!!
# Zerojudge e638


class Solution:
    def mainloop(self):
        while True:
            try:
                num = self.get_input()
            except EOFError:
                break
            else:
                print('YES' if num % 131071 == 0 else 'NO')
    
    @staticmethod
    def get_input() -> int:
        ipt = [input()]
        while ipt[-1][-1] != '#':
            ipt.append(input())
        return int(''.join(ipt).rstrip('#'), 2)


if __name__ == '__main__':
    s = Solution()
    s.mainloop()
