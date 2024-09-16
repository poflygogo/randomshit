age = int(input())

print(590 * (5 < age <= 11) + 790 * (11 < age <= 17) + 890 * (17 < age <= 59) + 399 * (age > 59))