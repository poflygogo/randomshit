# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i792. pB. 造橋人，我的超人


from itertools import accumulate

n = int(input())
board = list(map(int, input().split()))
gifts = list(map(int, input().split()))
board.sort(reverse=True)
print(sum(i * j for i, j in zip(accumulate(gifts), board[1:])))
