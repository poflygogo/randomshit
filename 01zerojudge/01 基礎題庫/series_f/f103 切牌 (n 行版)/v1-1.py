def main():
    n, k = map(int, input().split())
    arr = [input() for _ in range(n)]
    print(*arr[k:], *arr[:k], sep="\n")


main()
