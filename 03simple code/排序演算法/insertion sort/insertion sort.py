# -*- encoding: utf-8 -*-
# python 3.12
# insertion sort


def insertion_sort(arr):
    # in-place
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[i] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    print('original array: ', arr)
    insertion_sort(arr)
    print('sorted array' ,arr)
