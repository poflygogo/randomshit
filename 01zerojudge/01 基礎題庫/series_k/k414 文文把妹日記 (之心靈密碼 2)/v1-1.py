card1 = {int(i) for i in input().split()}
card2 = {int(i) for i in input().split()}
card3 = {int(i) for i in input().split()}
card4 = {int(i) for i in input().split()}
card5 = {int(i) for i in input().split()}

primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103,
    107, 109, 113, 127
]

result = {}
for p in primes:
    temp = [
        '1' if p in card1 else '0',
        '1' if p in card2 else '0',
        '1' if p in card3 else '0',
        '1' if p in card4 else '0',
        '1' if p in card5 else '0'
    ]
    result[p] = int(''.join(temp), 2)

primes.sort(key=lambda x: result[x])
print(*primes)
