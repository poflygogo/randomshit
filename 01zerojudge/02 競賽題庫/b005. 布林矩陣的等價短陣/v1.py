from sys import stdin

for num in stdin:
    num = int(num.strip())
    data = [list(map(int, stdin.readline().strip().split())) for _ in range(num)]

    even_row = list(map(lambda x: sum(x) % 2, data))
    even_col = [sum([data[row][col] for row in range(num)]) % 2 for col in range(num)]
    
    if sum(even_row) == sum(even_col) == 0:
        print('OK')

    elif sum(even_row) == sum(even_col) == 1:
        print(f'Change bit ({even_row.index(1) + 1},{even_col.index(1) + 1})')
    
    else:
        print('Corrupt')