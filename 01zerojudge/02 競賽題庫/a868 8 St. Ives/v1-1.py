# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a868. 8. St. Ives
# HP CodeWars 2010


from functools import reduce
from operator import mul


numbers = {
    'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5,
    'SIX': 6, 'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10,
    'ELEVEN': 11, 'TWELVE': 12, 'THIRTEEN': 13
}

counter = [[], []]
text = input().split()
counter[0].extend([text[1], text[4]])
counter[1].extend([1, numbers[text[3]]])

for _ in range(3):
    text = input().split()
    counter[0].append(text[4])
    counter[1].append(numbers[text[3]])

ask = input().rstrip().rstrip('?').rsplit(maxsplit=1)[1]

print(reduce(mul, counter[1][:counter[0].index(ask) + 1]), ask)
