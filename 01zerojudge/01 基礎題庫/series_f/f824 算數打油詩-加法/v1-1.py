from sys import stdin


xinese_num = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
              '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}
num_xinese = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五',
              6: '六', 7: '七', 8: '八', 9: '九'}
for line in stdin:
    line = line.strip()
    if line[1] not in '有又':
        print('謬')
    else:
        ans = sum((xinese_num[line[0]], xinese_num[line[2]]))
        if ans == 20:
            print('二十')
        
        elif ans == 10:
            print('十')
        
        elif ans > 10:
            print(f'十{num_xinese[ans % 10]}')
        
        else:
            print(num_xinese[ans])
