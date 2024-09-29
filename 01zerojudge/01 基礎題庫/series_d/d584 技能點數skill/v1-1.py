from sys import stdin


for data in stdin:
    data = data.rstrip().split()
    if data[0] == '0':
        print('0')
    
    else:
        level = int(data[1])
        result = sum(((level >= 120) * 3, (level >= 70), (level >= 30), (data[0] == '2' and level >= 8), (data[0] != '2' and level >= 10)))
        if data[0] == '2':
            print(sum((result, (level - 8) * 3 if level > 8 else 0)))
        
        else:
            print(sum((result, (level - 10) * 3 if level > 10 else 0)))
