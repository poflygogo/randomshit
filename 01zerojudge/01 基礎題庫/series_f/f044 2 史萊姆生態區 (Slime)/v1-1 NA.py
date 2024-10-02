import math


king_slime, slime = map(int, input().split())
gcd = math.gcd(king_slime, slime)
king_slime, slime = king_slime // gcd, slime // gcd
print(
    f'{math.log2((slime + 1) // 2 // king_slime) + 1:.0f}'
)
