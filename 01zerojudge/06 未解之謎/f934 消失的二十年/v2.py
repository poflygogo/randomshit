trend_data = tuple(map(int, input().split()))

subarray_sum_list = [0]
subarray_sum = 0
for numA, numB in zip(trend_data, trend_data[1:]):
    if numA <= numB:
        subarray_sum += numB - numA
    else:
        subarray_sum_list.append(subarray_sum)
        subarray_sum = 0
else:
    subarray_sum_list.append(subarray_sum)

print(max(subarray_sum_list))