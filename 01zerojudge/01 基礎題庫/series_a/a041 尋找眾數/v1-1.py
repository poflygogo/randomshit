# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a041. 尋找眾數


def mode(arr: list):
    counter = {}
    for i in arr:
        counter[i] = counter.get(i, 0) + 1
    target = max(counter.values())
    return sorted(filter(lambda x: counter[x] == target, counter))


def main():
    while True:
        try:
            arr = list(map(int, input().split()))
        except EOFError:
            break
        print(' '.join(map(str, mode(arr))))


if __name__ == '__main__':
    main()
