# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c679. 大家來出題 { 2: hello, World }


import random


class TestCaseGenerator:
    def __init__(self):
        self.seen = set()
        self.chr = {
            True: (65, 91),
            False: (97, 123)
        }
    
    def gen_text(self, target_length: int) -> str:
        result = []
        while not (any(65 <= i < 91 for i in result) and any(97 <= i < 123 for i in result)):
            result = [
                random.randrange(*self.chr[random.choice((True, False))])
                for _ in range(target_length)
            ]
        return ''.join(chr(i) for i in result)
    
    def main(self):
        w, v1, v2 = map(int, input().split())
        n = iter(range(v1, v2 + 1))
        while w > 0:
            target_length = next(n)
            if target_length == v2:
                n = iter(range(v1, v2 + 1))
            text = self.gen_text(target_length)
            if text in self.seen:
                continue
            w -= 1
            self.seen.add(text)
            print(f'{text}: hello, {text}')


if __name__ == '__main__':
    s = TestCaseGenerator()
    s.main()
