for i in range(int(input())):
    kingdom = input()
    print(
        f'Case #{i + 1}: {kingdom} is ruled by',
        'nobody.' if kingdom[-1] == 'y' else
        'Alice.' if kingdom[-1] in {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'} else
        'Bob.'
    )
