def sep_coordinates(data:str) -> tuple:
    for index, item in enumerate(data):
        if item.isdigit():
            break
    return data[:index], int(data[index:])

def letter_to_num(row_str) -> int:
    result = 0
    for index, item in enumerate(row_str[::-1]):
        result += (ord(item)-64) * 26 ** index
    return result

row, column = sep_coordinates(input())
print(letter_to_num(row) * column)