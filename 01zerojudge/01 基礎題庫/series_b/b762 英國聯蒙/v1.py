from sys import stdin, stdout

data = {3:'KILLING SPREE!\n' ,4:'RAMPAGE~\n', 5:'UNSTOPPABLE!\n', 6:'DOMINATING!\n', 7:'GUALIKE!\n'}

k, d, a, count = 0, 0, 0, 0
for _ in range(int(stdin.readline().strip())):
    state = stdin.readline().strip()
    if state == 'Get_Kill':
        k += 1
        count += 1
        if count < 3:
            stdout.write('You have slain an enemie.\n')
        elif count >= 8:
            stdout.write('LEGENDARY!\n')
        else:
            stdout.write(data[count])
    
    elif state == 'Get_Assist':
        a += 1
    
    else:
        d += 1
        if count < 3:
            stdout.write('You have been slained.\n')
        else:
            stdout.write('SHUTDOWN.\n')
        count = 0

stdout.write(f'{k}/{d}/{a}\n')