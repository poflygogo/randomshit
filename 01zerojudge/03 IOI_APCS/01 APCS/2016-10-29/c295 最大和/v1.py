N, _ = input().split()
data = [tuple(map(int, input().split())) for _ in range(int(N))]

nums = [max(i) for i in data]

sum = sum(nums)
factor = [i for i in nums if sum % i == 0]

print(sum)
if factor:
    print(*factor)
else:
    print(-1)