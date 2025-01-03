# -*- encoding: utf-8 -*-
# python 3.12


def my_permutation(iterable, visit=None, perm=None):
    if visit is None:
        visit = set()
    if perm is None:
        perm = []
    if visit and perm and len(iterable) == len(visit):
        print(perm)
        return
    for item in iterable:
        if item not in visit:
            perm.append(item)
            visit.add(item)
            my_permutation(iterable, visit, perm)
            perm.pop()
            visit.remove(item)


if __name__ == '__main__':
    my_permutation([1, 2, 3, 4])
