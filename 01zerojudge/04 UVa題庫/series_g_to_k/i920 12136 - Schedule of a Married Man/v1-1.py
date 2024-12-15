for i in range(1, int(input()) + 1):
    wife = [int(i) for i in input().replace(':', '').split()]
    work = [int(i) for i in input().replace(':', '').split()]
    print(
        f'Case {i}:',
        'Mrs Meeting' if not (wife[1] < work[0] or work[1] < wife[0]) else 'Hits Meeting'
    )
