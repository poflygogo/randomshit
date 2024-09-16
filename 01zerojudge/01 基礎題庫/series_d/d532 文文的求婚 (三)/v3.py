def check_is_leep(n:int) -> bool:
    return n % 4 == 0 and n % 100 != 0 or n % 400 == 0

yearA, yearB = sorted(map(int, input().split()))

count = 0
for year in range(yearA+((4-yearA%4)%4), yearB +1, 4):
    if check_is_leep(year):
        count += 1

print(count)