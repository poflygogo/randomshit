import re
from sys import stdin


stack = []
for time in stdin:
    time = re.findall(r'[\d\.]+|[\D]+', time.strip())
    result = 0
    for item in time:
        if '.' in item or item.isdecimal():
            stack.append(float(item))
        
        elif item in ('hour', 'h'):
            result += stack.pop() * 3600000
        
        elif item in ('min', 'm'):
            result += stack.pop() * 60000
        
        elif item == 's':
            result += stack.pop() * 1000
        
        else:
            result += stack.pop()
    
    print(f'{result: <.0f}')
