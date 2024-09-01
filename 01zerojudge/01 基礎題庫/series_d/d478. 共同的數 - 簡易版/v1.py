n, _ = map(int, input().split())

for _ in range(n):
    setA = set(input().split())
    setB = set(input().split())
    print(len(setA & setB))