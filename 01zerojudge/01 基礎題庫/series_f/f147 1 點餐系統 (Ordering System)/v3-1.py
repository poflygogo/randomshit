from sys import stdin


total = []
for command in stdin:
    command = int(command)
    if command == 0: break
    id = int(next(stdin))

    if command == 1:
        if id == 1:
            print('Medium Wac', 4)
            total.append(4)
        elif id == 2:
            print('WChicken Nugget', 8)
            total.append(8)
        elif id == 3:
            print('Geez Burger', 7)
            total.append(7)
        elif id == 4:
            print('ButtMilk Crispy Chicken', 6)
            total.append(6)
        else:
            print('Plastic Toy', 3)
            total.append(3)
    elif id == 1:
        print('German Fries', 2)
        total.append(2)
    elif id == 2:
        print('Durian Slices', 3)
        total.append(3)
    elif id == 3:
        print('WcFurry', 5)
        total.append(5)
    else:
        print('Chocolate Sunday', 7)
        total.append(7)
        

print(f'Total: {sum(total)}')
