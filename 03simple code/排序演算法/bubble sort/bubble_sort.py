# -*- encoding: utf-8 -*-
# python 3.12


class SortAlgorithm(list):
    def bubble_sort(nums: list[int]) -> None:
        length = len(nums)
        if length <= 1:
            return
        
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    my_list = [9, 8, 7, 6, 3, 4, 5, 2, 3, 1]
    my_list = SortAlgorithm(my_list)
    my_list.bubble_sort()
    print(my_list)
