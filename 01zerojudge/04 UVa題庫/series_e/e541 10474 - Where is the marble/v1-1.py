case = 0
while True:
    marbles, question = map(int, input().split())
    if marbles == question == 0:
        exit()

    marble = [int(input()) for _ in range(marbles)]
    marble.sort()

    case += 1
    print(f'CASE# {case}:')
    for _ in range(question):
        target = int(input())
        try:
            print(f'{target} found at {marble.index(target) + 1}')
        except ValueError:
            print(f'{target} not found')
