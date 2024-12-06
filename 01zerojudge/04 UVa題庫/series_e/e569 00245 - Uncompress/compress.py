def compress(text: str) -> str:
    from re import findall
    text: list[str] = findall(r'\w+|\W+', text)
    temp: list[str] = []
    for i in range(0, len(text), 2):
        try:
            idx = temp.index(text[i])
        except ValueError:
            temp.append(text[i])
        else:
            text[i] = str(len(temp) - idx)
            temp.append(temp.pop(idx))
    return ''.join(text)


my_text = "Dear Sally,\n\n    Please, please do it--it would please\nMary very, very much. And Mary would\ndo everything in Mary's power to make\nit pay off for you.\n\n    -- Thank you very much--\n"
print(compress(my_text))
