n, time = map(int, input().split())
book = {i: {1: j[0], 2: j[1]} for i, j in enumerate(tuple(map(int, input().split())) for _ in range(n))}

score = 0
for _ in range(time):
    chapter = max(book, key=lambda x: book[x][1])
    score += book[chapter][1]
    book[chapter][1] -= book[chapter][2]
    if book[chapter][1] < 0:
        book[chapter][1] == 0

print(score)
