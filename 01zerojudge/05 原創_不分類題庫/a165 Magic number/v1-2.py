# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a165. Magic number


def magic_number():
    def dfs(num: list, depth: int = 0):
        if depth == 9:
            nonlocal result
            result = ''.join(map(str, num))
            return True
        
        depth += 1
        if depth == 5:
            arr = [5]
        elif depth % 2 != 0:
            arr = item_odd
        else:
            arr = item_even
        
        for i in arr:
            if (len(num) < 2) or (i not in num and (int(''.join(map(str, num))) * 10 + i) % depth == 0):
                num.append(i)
                if dfs(num, depth):
                    return True
                num.pop()
    
    item_odd = [1, 3, 7, 9]
    item_even = [2, 4, 6, 8]
    result = None
    dfs([])
    return result


if __name__ == '__main__':
    print(magic_number())
