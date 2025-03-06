# -*- encoding: utf-8 -*-
# python 3.12


import random


def get_ans(n: int) -> str:
    result = [' ' * (n - i) + ' '.join('*' * i) for i in range(1, n + 1)]
    trunk = ' ' * (n - 2) + '| |'
    result.extend([trunk for _ in range(n // 2)])
    result.append('\\' + '_' * (n + (n - 1) - 2) + '/')
    return '\n'.join(result)


def setup_file(token: list[int], end: int, start: int = 0):
    token = iter(token)
    for i in range(start, end):
        n = next(token)
        with open(f'./q089_{i:02d}.in', 'w') as f:
            f.write(str(n) + '\n')
        with open(f'./q089_{i:02d}.out', 'w') as f:
            f.write(get_ans(n) + '\n')
    

def generate_problem():
    # 保證前 5 筆測資 <= 10
    setup_file(token=random.sample(range(2, 11), 5),
               start=0,
               end=5)
    
    # 保證 90% 的測資 <= 50
    setup_file(token=random.sample(range(11, 51), 18 - 5),
               start=5,
               end=18)
    
    # 第 19 筆測資的範圍為 50 < n < 100
    setup_file(token=[random.randint(51, 99)],
               start=18,
               end=19)
    
    # 第 20 筆的測資固定為 100
    setup_file(token=[100],
               start=19,
               end=20)


if __name__ == '__main__':
    generate_problem()
