from sys import stdin


soundex_code = {
    'B': '1', 'P': '1', 'F': '1', 'V': '1',
    'C': '2', 'S': '2', 'K': '2', 'G': '2', 'J': '2', 'Q': '2', 'X': '2', 'Z': '2',
    'D': '3', 'T': '3',
    'L': '4',
    'M': '5', 'N': '5',
    'R': '6'
}

print('NAME                     SOUNDEX CODE')
for name in stdin:
    name = name.rstrip()
    s_code = [name[0]]
    for char, pre in zip(name[1:], name):
        if char in soundex_code and soundex_code.get(pre, 0) != soundex_code[char]:
            s_code.append(soundex_code[char])
            if len(s_code) == 4:
                break 
    print(f'         {name:<20s}     {"".join(s_code):0<4s}')
print('                   END OF OUTPUT')


# zerojudge a131
# UVa 00739
# AC(17ms, 3.3MB)
# 2024-10-18
