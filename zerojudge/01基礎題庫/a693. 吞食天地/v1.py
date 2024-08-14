# n代表有幾種食物, m代表有幾組測資
n, m = map(int, input().split())

# n對python來說不重要, 作用相當於len()
food_data = tuple(map(int, input().split()))

for _ in range(m):
    l, r = map(lambda x: int(x) - 1, input().split())
    print(sum(food_data[l:r+1]))
