from sys import stdin, stdout

for line in stdin:
    line = line.split() 
    
    data = []
    for item in line:
        if item.isdecimal():
            data.append(int(item))
    
    if data:
        stdout.write(f'{sum(data)}\n')
    else:
        stdout.write('0\n')

# 我寫python的來這湊什麼熱鬧
