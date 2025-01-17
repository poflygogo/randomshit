# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e837 P4 字母排列 (Letters)
# 2019-08 TOI 新手同好會


def longest_contiguous_subsequence(s: str) -> tuple:
    max_sub_seq = 1, s[0]
    start = 0
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) != 1:
            if max_sub_seq[0] < i - start:
                max_sub_seq = i - start, s[start:i]
            elif max_sub_seq[0] == i - start:
                max_sub_seq = max_sub_seq[0], s[start:i]
            start = i
    if len(s) - start > max_sub_seq[0]:
        return len(s) - start, s[start:]
    if len(s) - start == max_sub_seq[0]:
        return max_sub_seq[0], s[start:]
    return max_sub_seq


if __name__ == '__main__':
    print(*longest_contiguous_subsequence(input()))
    # test = ['abcwkodvwxyzwia', 'gfeabuvstyzijo', 'apple']
    # for t in test:
    #     print(*longest_contiguous_subsequence(t))
