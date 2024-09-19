from sys import stdin
from statistics import mean


for track in range(1, int(next(stdin).strip()) + 1):
    data = [list(map(int, next(stdin).strip().split())) for _ in range(int(next(stdin).strip()))]
    best = min(data, key=lambda x: (x[0], x[1]))
    data = list(map(lambda x: x[0] * 60 + x[1], data))
    average = int(mean(data))
    print(
        f'Track {track}:',
        f'Best Lap: {best[0]} minute(s) {best[1]} second(s).',
        f'Average: {average // 60} minute(s) {average % 60} second(s).',
        sep='\n'
    )
