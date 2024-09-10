for _ in range(int(input())):
    a, b = map(int, input().split('+'))
    print('yes' if a + b == int(input()) else 'no')