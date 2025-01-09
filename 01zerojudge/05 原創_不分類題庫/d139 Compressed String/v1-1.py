# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d139. Compressed String


from itertools import groupby


def main():
    while True:
        try:
            text = input()
        except EOFError:
            break
        print(compressed_string(text))


def compressed_string(text: str):
    result = []
    for key, val in groupby(text):
        length = len(tuple(val))
        result.append(
            key * length if length < 3 else
            str(length) + key
        )
    return ''.join(result)


if __name__ == '__main__':
    main()
