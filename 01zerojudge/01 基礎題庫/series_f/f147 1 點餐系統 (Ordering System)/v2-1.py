from sys import stdin


total = []
for command in stdin:
    command = command.strip()
    if command == '0': break

    id = int(next(stdin).strip()) - 1

    if command == '1':
        print(
            ("Medium Wac", "WChicken Nugget", "Geez Burger", "ButtMilk Crispy Chicken", "Plastic Toy")[id],
            (4, 8, 7, 6, 3)[id]
        )
        total.append((4, 8, 7, 6, 3)[id])

    else:
        print(
            ("German Fries", "Durian Slices", "WcFurry", "Chocolate Sunday")[id],
            (2, 3, 5, 7)[id]
        )
        total.append((2, 3, 5, 7)[id])
        

print(f'Total: {sum(total)}')
