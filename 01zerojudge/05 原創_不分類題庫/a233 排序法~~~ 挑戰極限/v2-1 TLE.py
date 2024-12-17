# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a233
# 
# 自己實現 merge sort


def main():
    from sys import stdin, stdout
    n = int(stdin.readline().rstrip())
    nums = stdin.readline().rstrip().split()
    stdout.write(' '.join(str(i) for i in mergeSort(nums)))


def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    while left and right:
        if int(left[0]) <= int(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


main()
