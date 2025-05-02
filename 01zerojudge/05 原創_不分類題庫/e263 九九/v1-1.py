# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e263. 九九


while True:
    try:
        n, _ = map(int, input().split())
        cards = input().split()
    except EOFError:
        break

    player_id = 0
    turn = 1
    score = 0
    for card in cards:
        if card == 'A':
            score = 0
        elif card == '4':
            turn *= -1
        elif '5' in card:
            card = card.strip('5').strip(f'()')
            player_id = int(card) - 1
            continue
        elif card == '10+':
            score += 10
        elif card == '10-':
            score -= 10
            if score < 0:
                score = 0
        elif card == 'J':
            pass
        elif card == 'Q+':
            score += 20
        elif card == 'Q-':
            score -= 20
            if score < 0:
                score = 0
        elif card == 'K':
            score = 99
        else:
            score += int(card)
        
        if score > 99:
            print(f'{player_id + 1} cheated!')
            break
        player_id = (player_id + turn) % n
    else:
        print(f'The sum is {score}')
