target = input().split()
ticket = input().split()
check = [ticket.count(item) for item in target]
print(min(check))