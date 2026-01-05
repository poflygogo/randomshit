# ZeroJudge r860
# TOI 練習賽 新手組 第三題 符文 (Runes)
# python 3.8


def find(arr: list[int], sub_arr: list[int]):
    sub_arr_size = len(sub_arr)
    for i in range(len(arr)):
        if arr[i : i + sub_arr_size] == sub_arr:
            return i + 1
    return "not found"


def main():
    input()
    arr = list(map(int, input().split()))
    sub_arr = list(map(int, input().split()))

    print(find(arr, sub_arr))


main()
