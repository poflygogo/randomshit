deck = [
    i + j
    for i in "SHDF"
    for j in ["A"] + list(map(str, range(2, 11))) + ["J", "Q", "K"]
]

for _ in range(int(input())):
    command = input().split()
    if command[0] == "1":
        a, b = map(int, command[1:])
        deck = deck[a - 1 : b] + deck
        del deck[a + (b - a) : b + b - a + 1]
    elif command[0] == "2":
        a, b = map(int, command[1:])
        deck.extend(deck[a - 1 : b])
        del deck[a - 1 : b]
    elif command[0] == "3":
        k = int(command[1])
        deck = deck[-k:] + deck[:-k]
    elif command[0] == "4":
        k = int(command[1])
        deck.extend(deck[:k])
        del deck[:k]
    else:
        assert False, f"[Error] what is {command=}"

print(*deck[:5])
