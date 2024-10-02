king_slime, slime = map(int, input().split())

day = 0
while 2 ** day != (king_slime + slime) // king_slime:
    day += 1
print(day)
