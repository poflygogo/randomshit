from sys import stdin


for num in stdin:
    print(
        sum(
            2 if digit == '8' else 1 for digit in num.strip() if digit in '0689'
        )
    )
