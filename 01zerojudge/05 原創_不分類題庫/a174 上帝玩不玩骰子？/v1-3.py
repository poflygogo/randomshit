# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a174. 上帝玩不玩骰子？


def god_play_dice(k: int, m: int):
    data = [list() for _ in range(m)]
    for _ in range(k):
        comm = input().split()
        if comm[0] == '1':
            if int(comm[1]) not in data[int(comm[1]) % m]:
                data[int(comm[1]) % m].append(int(comm[1]))
        elif comm[0] == '2':
            if int(comm[1]) in data[int(comm[1]) % m]:
                data[int(comm[1]) % m].remove(int(comm[1]))
        else:
            print(
                '===== s =====',
                '\n'.join(f'[{i:03d}]:' + ' -> '.join(map(str, sorted(j) + ['NULL'])) for i, j in enumerate(data)),
                '===== e =====',
                sep='\n'
            )


def main():
    while True:
        try:
            k, m = map(int, input().split())
        except EOFError:
            break
        else:
            god_play_dice(k, m)


if __name__ == '__main__':
    main()
