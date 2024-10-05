n = int(input())
ans = f'{sum(map(int, input().split())) / n:.2f}'
print(ans.rstrip('0').rstrip('.'))
