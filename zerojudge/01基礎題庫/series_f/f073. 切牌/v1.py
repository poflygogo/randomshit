length = int(input())
card = input().split()
cut = int(input())

print(*card[cut:],*card[:cut])