# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a631. 11. LED Decoder
# HP CodeWars 2007


from re import findall


code = {
    '0': ' ', '123457': 'A', '1234567': 'B', '456': 'C', '1580': 'D', '12456': 'E', '1249': 'F',
    '12569': 'G', '13457': 'H', '37': 'I', '3567': 'J', '13459': 'K',
    '156': 'L', '12357': 'M', '3579': 'N', '123567': 'O', '1458': 'P',
    '12347': 'Q', '123459': 'R', '12467': 'S', '278': 'T', '13567': 'U',
    '1379': 'V', '135790': 'W', '90': 'X', '1347': 'Y', '23456': 'Z'
}

while True:
    try:
        text = input().rstrip()
    
    except EOFError:
        break

    else:
        result = []
        item: str
        for item in findall(r'\d+|\D+', text):
            if not item.isdecimal():
                result.append(item)
                continue
            
            while item != '':
                idx = 1
                while item[:idx] not in code:
                    idx += 1
                result.append(code[item[:idx]])
                item = item[idx:]
        
        print(''.join(result))
