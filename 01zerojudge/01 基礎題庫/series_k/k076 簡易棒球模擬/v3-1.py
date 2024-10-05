status = int(input().replace(' ', ''), 2)
status = (status << 1) + 1
run = int(input())
status = status << (run - 1)
status = bin(status)
print(
    sum(i == '1' for i in status[2: 2 + run]),
    ' '.join([i for i in status[-3:]]),
    sep='\n'
)
