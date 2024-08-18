def check_is_leep(n:int) -> bool:
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return True
    else:
        return False

yearA, yearB = sorted(map(int, input().split()))

count = 0
for year in range(yearA, yearB +1):
    if check_is_leep(year):
        count += 1

print(count)