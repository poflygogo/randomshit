def Evaluate(Name: str):
    if(type(Name) != str):
        return -1

    Score = 0
    NameLen = len(Name)

    for i in range(NameLen):
        CharCode = ord(Name[i])
        Score += ((CharCode * 1123) % 1002)

        while (CharCode > 0):
            Score += (CharCode % 10)
            CharCode = (CharCode // 10)

    return (Score % 101)


data = []
for i in range(int(input())):
    name = input()
    score = Evaluate(name)
    data.append((i, name, score))

data.sort(key=lambda x: x[2])
for _, name, score in data:
    print(name, score)
