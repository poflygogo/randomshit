trend_data = tuple(map(int, input().split()))

trend_data_analyze = [item-trend_data[idx] for idx, item in enumerate(trend_data[1:])]

subarray_sum_list = [0]
subarray_sum = 0
for item in trend_data_analyze:
    if item >= 0:
        subarray_sum += item
    else:
        subarray_sum_list.append(subarray_sum)
        subarray_sum = 0

print(max(subarray_sum_list))