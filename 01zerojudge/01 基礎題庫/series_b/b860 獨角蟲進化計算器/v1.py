candy, weedle = map(int, input().split())

time = 0
while candy > 12 or candy + weedle > 12:
    # 糖果充足
    if candy >= 12:
        candy -= 10
        weedle -= 1
    
    # 糖果不足
    else:
        candy = 2
        weedle -= 11 - candy
    
    time += 1

print(time)