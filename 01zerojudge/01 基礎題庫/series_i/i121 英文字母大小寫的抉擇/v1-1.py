sentence = input()
command = input()

sentence = sentence.lower()
if command == '1':
    print(sentence.capitalize())
elif command == '2':
    print(sentence.upper())
elif command == '3':
    print(sentence.title())
else:   # command == '4'
    print(sentence)
