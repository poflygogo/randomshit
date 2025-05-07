# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e168. 演唱會記行 - 周邊商品確認


def unpack_the_gift(gift: str) -> str:
    if len(gift) % 2 != 0:
        return 'Product Broken!!'
    pair = {'}': '{', ')': '(', ']': '['}
    result = []
    stack = []
    cnt = 0
    for i in gift:
        if i not in pair:
            stack.append(i)
            cnt += 1
            if cnt > 1:
                result.append(i)
        elif stack and stack[-1] == pair[i]:
            stack.pop()
            cnt -= 1
            if cnt > 0:
                result.append(i)
        else:
            return 'Product Broken!!'
    if result:
        return ''.join(result)
    else:
        return 'Product Broken!!'


def main():
    n = int(input())
    while n:
        for _ in range(n):
            gift = input()
            print(unpack_the_gift(gift))
        n = int(input())


if __name__ == '__main__':
    main()
