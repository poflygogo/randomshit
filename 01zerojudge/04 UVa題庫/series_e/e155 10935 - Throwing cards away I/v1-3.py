
while True:
    n = int(input())
    if not n:
        exit()
        
    discard = []
    card = [i for i in range(n, 0, -1)]
    while card.__len__() > 1:
        discard.append(str(card.pop()))
        card.insert(0, card.pop())
    
    print(
        f'Discarded cards: {", ".join(discard)}',
        f'Remaining card: {card.pop()}',
        sep='\n'
    )
