from fractions import Fraction


r = Fraction(input())
R = (r * 9) / 5 + 32
print(int(R) if R.denominator == 1 else float(R))
