# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00101 The Blocks Problem
# ZeroJudge c073


def reset(arr: list, t: int):
    while arr[-1] != t:
        k = arr.pop()
        blocks[k].append(k)
        locate[k] = k


while True:
    try:
        n = int(input())
        blocks = [[i] for i in range(n)]
        locate = list(range(n))
        ipt = input()
        while not ipt.startswith('quit'):
            act, a, mode, b = ipt.split()
            a, b = int(a), int(b)

            # ignore invalid movement
            if a == b or locate[a] == locate[b]:
                pass

            elif act == 'move':
                reset(blocks[locate[a]], a)
                if mode == 'onto':
                    reset(blocks[locate[b]], b)
                blocks[locate[b]].append(blocks[locate[a]].pop())
                locate[a] = locate[b]

            elif act == 'pile':
                if mode == 'onto':
                    reset(blocks[locate[b]], b)
                idx = blocks[locate[a]].index(a)
                blocks[locate[b]].extend(blocks[locate[a]][idx:])
                for i in range(idx + 1, len(blocks[locate[a]])):
                    locate[blocks[locate[a]][i]] = locate[b]
                del blocks[locate[a]][idx:]
                locate[a] = locate[b]

            ipt = input()

        for i in range(n):
            print(f'{i}:', ' '.join(map(str, blocks[i])))
    except EOFError:
        break
