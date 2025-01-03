# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e780. 禮物拋接遊戲


def main():
    x   = 0
    cnt = 0
    for _ in range(int(input())):
        action = input().split()
        if action[0] == 'L':
            x -= 1
        elif action[0] == 'R':
            x += 1
        elif int(action[1]) == x:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
