# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10903 Rock-Paper-Scissors Tournament
# ZeroJudge j604


def main():
    while True:
        ipt = input().split()
        if ipt[0] == '0':
            break
        data = get_game_result(*map(int, ipt))
        print(summary(data))


def get_game_result(n, k) -> list:
    win = {('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')}
    result = [[0, 0] for _ in range(n)]
    for _ in range(k * n * (n - 1) // 2):
        id1, act1, id2, act2 = input().split()
        id1, id2 = map(lambda x: int(x) - 1, (id1, id2))
        if act1 == act2:
            continue
        if (act1, act2) not in win:
            id1, id2 = id2, id1
        result[id1][0] += 1
        result[id2][1] += 1
    return result


def summary(data: list) -> str:
    result = [f'{i[0] / sum(i):.3f}' if sum(i) != 0 else '-' for i in data]
    return '\n'.join(result)


main()
