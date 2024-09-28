from sys import stdin
import decimal


for line in stdin:
    ans = round(decimal.Decimal(line.strip()), 2)
    if ans == -0.00:
        print('0.00')
    else:
        print(ans)
