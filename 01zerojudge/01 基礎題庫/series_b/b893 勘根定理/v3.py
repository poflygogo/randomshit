from sys import stdin, stdout

def zi_func(n:int) -> int:
    """
    可能經常重複執行的的語句就定義成函數
    求 f(x) 的值
    """
    return (a * n ** 5) + (b * n ** 4) + (c * n ** 3) + (d * n ** 2) + (e * n) + f

a, b, c, d, e, f = map(int, stdin.readline().strip().split())

# 若所有值都是 0 ，代表與x軸重合，有無限多解
# 若除了f外所有值都是0，代表與x軸平行，無解
if a == b == c == d == e == 0:
    if f:
        stdout.write(r'N0THING! >\\\<')
    else:
        stdout.write('Too many... = ="')
else:
    result = []     # 把結果存起來，後面一起送出去

    # 勘根定理
    # 用 zip() 搭配 range() 取要傳入的值
    for i, j in zip(range(-35, 35), range(-34, 36)):
        func_i = zi_func(i)
        func_j = zi_func(j)
        if func_i * func_j < 0:
            result.append(f'{i} {j}')

        elif func_i * func_j == 0:
            if func_i == 0:
                result.append(f'{i} {i}')

    # 如果全部循環完，result 裡面仍是空的，代表無解
    if result:
        result = '\n'.join(result)
        stdout.write(result)
    else:
        stdout.write(r'N0THING! >\\\<')