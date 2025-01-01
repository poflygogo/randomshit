# -*- encoding: utf-8 -*-
# python 3.12


def quick_sort(arr, left, right):
    if left < right:    
        mid   = partition(arr, left, right)
        left  = quick_sort(arr, left, mid - 1)
        right = quick_sort(arr, mid + 1, right)
    

def partition(arr, left, right):
    pivot = arr[right]
    i     = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


if __name__ == '__main__':
    my_arr = [10, 7, 8, 9, 1, 5]
    quick_sort(my_arr, 0, len(my_arr) - 1)
    print(my_arr)
