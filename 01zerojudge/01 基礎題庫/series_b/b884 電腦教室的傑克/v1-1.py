for _ in range(int(input())):
    yee = 100 - sum(map(int, input().split()))
    print(
        'sad!' if 0 < yee <= 30 else
        'hmm~~' if 30 < yee <= 60 else
        'Happyyummy' if 60 < yee < 100 else
        'evil!!'
    )
