from sys import stdin


data = [tuple(map(int, i.strip().split())) for i in stdin]
data.sort(key=lambda x: x[0], reverse=True)
print(
    *[f'{i}元鈔票共有{j}張' for i, j in data],
    f'總共有{sum([i * j for i, j in data])}元',
    sep='\n'
)
