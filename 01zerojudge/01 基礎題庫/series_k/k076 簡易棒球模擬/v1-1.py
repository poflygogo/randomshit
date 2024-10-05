status = [int(i) for i in input().split()]
run = int(input())
print(
    sum(status[:run]) if run < 4 else sum(status) + 1
)

status.extend([1] + [0] * (run - 1))
print(*status[run: run + 3])
