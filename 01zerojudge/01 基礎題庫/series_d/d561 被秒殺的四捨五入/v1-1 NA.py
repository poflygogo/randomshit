from sys import stdin
import decimal


decimal.getcontext().prec = 3

for line in stdin:
    print(round(decimal.Decimal(line.strip()), 2))
