import re
from sys import stdin


for data in stdin:
    data = re.findall(r'[\d\.]+|[\D]+', data.strip())
    result = 0
    for i in range(0, len(data), 2):
        if data[i + 1] in ('gb', 'g'):
            result += float(data[i]) * 8 * 10 ** 9
        
        elif data[i + 1] in ('mb', 'm'):
            result += float(data[i]) * 8 * 10 ** 6
        
        elif data[i + 1] in ('kb', 'k'):
            result += float(data[i]) * 8 * 10 ** 3
        
        elif data[i + 1] == 'byte':
            if data[i].isdecimal():
                result += int(data[i]) * 8
            
            else:
                temp = data[i].split('.')
                result += int(temp[0]) * 8 + int(temp[1])
        
        else:
            result += float(data[i])
    
    print(f'{result: <.0f}')
