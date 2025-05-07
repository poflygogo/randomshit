# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c672. RGB ⇆ HEX


def main():
    while True:
        try:
            color_info = input().rstrip()
        except EOFError:
            break

        if color_info[0] == '#':
            print(hex_to_RGB(color_info))
        else:
            print(RGB_to_hex(color_info))


def RGB_to_hex(data: str) -> str:
    data = data.split()
    return '#' + ''.join(hex(int(i))[2:].zfill(2) for i in data).upper()


def hex_to_RGB(data: str) -> str:
    return ' '.join(str(int(data[i:i + 2], 16)).upper() for i in range(1, 7, 2))


if __name__ == '__main__':
    main()
