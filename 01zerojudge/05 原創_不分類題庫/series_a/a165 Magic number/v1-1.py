# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a165. Magic number


def magic_number():
    def dfs(num: list, depth: int):
        if depth == 9:
            nonlocal result
            result = ''.join(map(str, num))
            return False
        
        # 能被 5 整除
        if depth == 4:
            dfs(num, depth + 1)
        else:
            arr = item_odd if depth % 2 == 0 else item_even
            for i in range(4):
                if arr[i] in num:
                    continue
                # 能被 1 或 2 整除
                if depth in (0, 1):
                    pass
                # 能被 3 或 6 整除
                elif depth in (2, 5) and (sum(num[:depth + 1]) + arr[i]) % 3 != 0:
                    continue
                # 能被 7 整除
                elif depth == 6 and int(''.join(map(str, num))) % 7 != 0:
                    continue
                # 能被 9 整除
                elif depth == 8 and sum(num) % 9 != 0:
                    continue
                # 能被 4 整除
                elif depth == 3 and (10 * num[2] + arr[i]) % 4 != 0:
                    continue
                # 能被 8 整除
                elif depth == 7 and (100 * num[5] + 10 * num[6] + arr[i]) % 8 != 0:
                    continue

                num[depth] = arr[i]
                dfs(num, depth + 1)
                num[depth] = 0

    item_odd = [1, 3, 7, 9]
    item_even = [2, 4, 6, 8]
    num = [0] * 9
    num[4] = 5
    result = None
    dfs(num, 0)
    return result


print(magic_number())
