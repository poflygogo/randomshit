cards = input().split()
for _ in range(int(input())):
    a, b = sorted(tuple(map(int, input().split())))
    cards.insert(b, cards.pop(a))
    cards.insert(a, cards.pop(b - 1))


print(*cards)

stu = tuple(map(int, input().split()))
jokeridx = cards.index('Joker')
target = stu.index(jokeridx)
print(target + 1)