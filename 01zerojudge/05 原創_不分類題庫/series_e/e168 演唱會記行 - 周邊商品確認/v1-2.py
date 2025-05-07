# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e168. 演唱會記行 - 周邊商品確認


def unpack_the_gift(gift: str) -> str:
    ERROR_MESSAGE = 'Product Broken!!'
    if len(gift) % 2 != 0:
        return ERROR_MESSAGE
    
    pair = {'}': '{', ')': '(', ']': '['}
    result = []
    stack = []
    depth = max_depth = 0
    for i in gift:
        if i not in pair:
            stack.append(i)
            if depth > 0:
                result.append(i)
            depth += 1
            max_depth = max(max_depth, depth)
        
        elif stack and stack[-1] == pair[i]:
            stack.pop()
            depth -= 1
            if depth > 0:
                result.append(i)
            elif depth == 0:
                if max_depth == 1:
                    return ERROR_MESSAGE
                else:
                    max_depth = 0

        else:
            return ERROR_MESSAGE
    
    if result:
        return ''.join(result)
    else:
        return ERROR_MESSAGE


def main():
    n = int(input())
    while n:
        for _ in range(n):
            gift = input()
            print(unpack_the_gift(gift))
        n = int(input())


if __name__ == '__main__':
    main()
