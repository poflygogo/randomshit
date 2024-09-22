n = int(input())
data = list(map(int, input().split()))
counter = [data.count(i) for i in range(1, 53)]
min_num, max_num = min(counter), max(counter)
print(
    min_num,
    (max_num - min_num) * 52 - (n - min_num * 52)
)
