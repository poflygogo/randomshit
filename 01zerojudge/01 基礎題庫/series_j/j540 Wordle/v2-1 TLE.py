answer = input()
counter = {i: answer.count(i) for i in set(answer)}

for _ in range(int(input())):
    flag = False
    while True:
        guess = input().rstrip()
        if guess == '#':
            print()
            break

        if flag:
            continue

        if guess == answer:
            flag = True
            print('OOOOO\nCongradulat1ons ! You guessed 1 times')
        elif len(guess) > 5:
            print('Too long')
        elif len(guess) < 5:
            print('Not enough letters')

        else:
            temp_counter = counter.copy()
            result = ['X'] * 5
            for i in range(5):
                if guess[i] == answer[i]:
                    result[i] = 'O'
                    temp_counter[guess[i]] -= 1
                elif guess[i] in answer:
                    result[i] = 'Y'
                    temp_counter[guess[i]] -= 1

            for i in range(4, -1, -1):
                if result[i] != 'Y':
                    continue
                if temp_counter[guess[i]] < 0:
                    result[i] = 'X'
                    temp_counter[guess[i]] += 1

            print(*result, sep='')
