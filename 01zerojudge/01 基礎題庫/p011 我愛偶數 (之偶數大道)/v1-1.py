from bisect import bisect_left


def main():
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    for i in map(int, input().split()):
        res += bisect_left(arr, i)
    print((res + n) * 2)


main()
