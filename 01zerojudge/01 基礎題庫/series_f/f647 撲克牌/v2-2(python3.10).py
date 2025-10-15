from collections import deque

deck = deque(
    i + j
    for i in "SHDF"
    for j in ["A"] + list(map(str, range(2, 11))) + ["J", "Q", "K"]
)

for _ in range(int(input())):
    command = input().split()
    match command[0]:
        case "1":
            a, b = map(int, command[1:])
            tmp = [deck[i] for i in range(b - 1, a - 2, -1)]
            for _ in range(b - a + 1):
                del deck[a - 1]
            deck.extendleft(tmp)
        case "2":
            a, b = map(int, command[1:])
            deck.extend(deck[i] for i in range(a - 1, b))
            for _ in range(b - a + 1):
                del deck[a - 1]
        case "3":
            deck.rotate(int(command[1]))
        case "4":
            for _ in range(int(command[1])):
                deck.append(deck.popleft())

print(" ".join(deck[i] for i in range(5)))
