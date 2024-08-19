def letter_to_num(row_str) -> int:
    result = 0
    for index, item in enumerate(row_str[::-1]):
        result += (ord(item)-64) * 26 ** index
    return result

num1, num2 = input().split()
print(letter_to_num(num2)-letter_to_num(num1)+1)