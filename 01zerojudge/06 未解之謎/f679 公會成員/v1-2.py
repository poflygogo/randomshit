# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f679. 公會成員


def main():
    n, q = map(int, input().split())
    members = input().split()
    for i in range(n):
        members[i] = int(members[i])
    for _ in range(q):
        print('Yes' if is_member(members, n, int(input())) else 'No')


def is_member(arr, length, id):
    lft, rgt = 0, length - 1
    while lft <= rgt:
        mid = (lft + rgt) // 2
        if arr[mid] == id:
            return True
        if arr[mid] < id:
            lft = mid + 1
        else:
            rgt = mid - 1
    return False


if __name__ == '__main__':
    main()
