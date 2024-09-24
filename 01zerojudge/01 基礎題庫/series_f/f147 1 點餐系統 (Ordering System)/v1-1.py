from sys import stdin


menu = {
    '1': {
        '1': ('Medium Wac', 4),
        '2': ('WChicken Nugget', 8),
        '3': ('Geez Burger', 7),
        '4': ('ButtMilk Crispy Chicken', 6),
        '5': ('Plastic Toy', 3)
    },
    '2': {
        '1': ('German Fries', 2),
        '2': ('Durian Slices', 3),
        '3': ('WcFurry', 5),
        '4': ('Chocolate Sunday', 7)
    }
}

total = 0
for command in stdin:
    command = command.strip()
    if command == '0': break

    target = menu[command][next(stdin).strip()]
    total += target[1]
    print(*target)

print(f'Total: {total}')
