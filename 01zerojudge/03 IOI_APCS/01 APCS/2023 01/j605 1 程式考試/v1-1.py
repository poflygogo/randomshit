time, score = [], []
for _ in range(int(input())):
    t, s = map(int, input().split())
    time.append(t)
    score.append(s)

total_score = max(score) - len(score) - 2 * score.count(-1)
print(
    total_score if total_score > 0 else 0,
    time[score.index(max(score))]
)
