# -*- uft-8 -*-
# python 3.12
# UVa 00136 Ugly Numbers
# LeetCode 264 Ugly Number II


def main():
    TARGET = 1500
    ugly = [1]
    p2 = p3 = p5 = 0
    while len(ugly) < TARGET:
        while ugly[p2] * 2 <= ugly[-1]:
            p2 += 1
        while ugly[p3] * 3 <= ugly[-1]:
            p3 += 1
        while ugly[p5] * 5 <= ugly[-1]:
            p5 += 1
        ugly.append(min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5))

    print(f"The 1500'th ugly number is {ugly[-1]}.")


main()
