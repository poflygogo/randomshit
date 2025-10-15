deck = [
    i + j
    for i in "SHDF"
    for j in ["A"] + list(map(str, range(2, 11))) + ["J", "Q", "K"]
]

for _ in range(int(input())):
    command = input().split()
    match command[0]:
        case "1":
            a, b = map(int, command[1:])
            deck = deck[a - 1 : b] + deck
            del deck[a + (b - a) : b + b - a + 1]
        case "2":
            a, b = map(int, command[1:])
            deck.extend(deck[a - 1 : b])
            del deck[a - 1 : b]
        case "3":
            k = int(command[1])
            deck = deck[-k:] + deck[:-k]
        case "4":
            k = int(command[1])
            deck.extend(deck[:k])
            del deck[:k]
        case _:
            assert False, f"[Error] what is {command=}"

print(*deck[:5])
