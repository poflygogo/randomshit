# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d139. Compressed String


def main():
    while True:
        try:
            text = input()
        except EOFError:
            break
        print(compressed_string(text))


def compressed_string(text: str):
    if len(text) <= 2:
        return text
    result = []
    cnt = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            cnt += 1
        else:
            result.append(
                text[i - 1] * cnt if cnt < 3 else
                str(cnt) + text[i - 1]
            )
            cnt = 1
        
        if i == len(text) - 1:
            result.append(
                text[i] * cnt if cnt < 3 else
                str(cnt) + text[i]
            )
    return ''.join(result)


if __name__ == '__main__':
    main()
