from sys import stdin


for track in range(1, int(next(stdin).strip()) + 1):
    n = int(next(stdin).strip())
    data = [list(map(int, next(stdin).strip().split())) for _ in range(n)]
    best = min(data, key=lambda x: (x[0], x[1]))
    average = sum(map(lambda x: x[0] * 60 + x[1], data)) // n
    print(
        f'Track {track}:',
        f'Best Lap: {best[0]} minute(s) {best[1]} second(s).',
        f'Average: {average // 60} minute(s) {average % 60} second(s).\n',
        sep='\n'
    )