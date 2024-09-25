from sys import stdin


[print(sum(2 if digit == '8' else 1 for digit in num.strip() if digit in '0689')) for num in stdin]
