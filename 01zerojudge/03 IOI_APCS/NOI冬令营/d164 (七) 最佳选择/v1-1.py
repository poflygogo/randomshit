from sys import stdin


for line in stdin:
    cows, buy = map(int, line.rstrip().split())
    prefix = [0]
    for _ in range(cows):
        prefix.append(prefix[-1] + int(stdin.readline().rstrip()))

    result = [prefix[i + buy] - prefix[i] for i in range(cows - buy + 1)]
    result.extend([prefix[-1] - prefix[i] + prefix[buy + i - cows] for i in range(cows - buy + 1, cows)])

    print(max(result))
