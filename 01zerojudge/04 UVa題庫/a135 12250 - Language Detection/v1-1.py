from sys import stdin


dictionary = {
    'HELLO': 'ENGLISH', 'HOLA': 'SPANISH', 'HALLO': 'GERMAN',
    'BONJOUR': 'FRENCH', 'CIAO': 'ITALIAN', 'ZDRAVSTVUJTE': 'RUSSIAN'
}
i = 1
while True:
    word = stdin.readline().rstrip()
    if word == '#':
        break

    print(f'Case {i}: {dictionary.get(word, "UNKNOWN")}')
    i += 1
