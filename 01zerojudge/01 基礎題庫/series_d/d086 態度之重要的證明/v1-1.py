from sys import stdin


for line in stdin:
    line = line.strip()
    if line == '0':
        break

    line = line.upper()
    total = 0
    for char in line:
        ascll = ord(char) - 64
        if 0 < ascll < 27:
            total += ascll
        
        else:
            print('Fail')
            break
    
    else:
        print(total)
