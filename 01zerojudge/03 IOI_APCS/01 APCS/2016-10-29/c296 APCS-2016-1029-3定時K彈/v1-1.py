# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c296. APCS-2016-1029-3定時K彈
# APCS-2016-1029


def main():
    n, m, k = map(int, input().split())
    print(time_bomb(n, m, k))


def time_bomb(n, m, k) -> int:
    """
    n 個人，每 m 個人爆炸一次，炸彈只爆炸 k 次。
    返回炸彈最後一次爆炸後的下一個人。
    """
    players = list(range(1, n + 1))
    
    def simulator(players: list, k: int, curr_idx: int=0):
        if k == 0:
            return players[curr_idx]
        curr_idx = (curr_idx + m - 1) % len(players)
        return simulator(players[:curr_idx])


# print(time_bomb(5, 2, 4))
