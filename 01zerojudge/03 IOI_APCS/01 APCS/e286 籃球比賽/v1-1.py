game = [sum(map(int, input().split())) for _ in range(4)]
result = sum([1 if game[i] > game[i + 1] else 0 if game[i] == game[i + 1] else -1 for i in range(0, 3, 2)])
print(
    f'{game[0]}:{game[1]}',
    f'{game[2]}:{game[3]}',
    'Win' if result > 0 else
    'Lose' if result < 0 else
    'Tie',
    sep='\n'
)
