# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b771. 46. Play with Words


from sys import stdin
from collections import deque, defaultdict
from itertools import groupby


def operate(text: deque, comm: str):
    if comm.startswith('insert left'):
        text.appendleft(comm.rsplit(maxsplit=1)[-1])
    
    elif comm.startswith('insert right'):
        text.append(comm.rsplit(maxsplit=1)[-1])
    
    elif comm.startswith('insert'):
        _, idx, t = comm.split()
        text.insert(int(idx) - 1, t)
    
    elif comm.startswith('delete left'):
        text.popleft()
    
    elif comm.startswith('delete right'):
        text.pop()

    # elif command.startswith('delete')
    else:
        del text[int(comm.split()[1]) - 1]


def longest_consecutive_sequence(text: deque) -> tuple[list, int]:
    counter = defaultdict(list)
    for i, j in groupby(text):
        counter[len(tuple(j))].append(i)
    if counter:
        max_length = max(counter)
        return counter[max_length], max_length
    else:
        return [], 0


def main():
    text = deque()
    for command in stdin:
        operate(text, command)
    max_length_elements, max_length = longest_consecutive_sequence(text)
    print(' '.join(max_length_elements), max_length)


if __name__ == '__main__':
    main()
