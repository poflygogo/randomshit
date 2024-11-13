case = 0
while True:
    n = int(input())
    if not n:
        exit()

    case += 1
    bricks = [int(i) for i in input().split()]
    average = sum(bricks) // n
    print(
        f'Set #{case}',
        f'The minimum number of moves is {sum(i - average for i in bricks if i > average)}.',
        sep='\n',
        end='\n\n'
    )
