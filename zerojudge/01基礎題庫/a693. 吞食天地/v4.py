from itertools import accumulate
while True:
    try:
        n, m = map(int, input().split())
        food_data = tuple(map(int, input().split()))
        food_data_prefix_sum = [0] + list(accumulate(food_data))

        for _ in range(m):
            l, r = map(int, input().split())
            print(food_data_prefix_sum[r]-food_data_prefix_sum[l-1])
    except EOFError:
        break
