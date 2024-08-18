yearA, yearB = sorted(map(int, input().split()))

print(
    (yearB // 4 - yearB // 100 + yearB // 400) -
    ((yearA-1) // 4 - (yearA-1) // 100 + (yearA-1) // 400)
)