# python 3.8
# ZeroJudge g310. pD. 甜甜圈大對決(Donut)


def main():
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    cnt = 0
    i = j = n - 1
    while i >= 0 and j >= 0:
        if arr1[i] < arr2[j]:
            cnt += 1
            j -= 1
        i -= 1
    print(cnt)


main()
