# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b983. NOIP2012 Day1.1.Vigenère密码
# NOIP 2012 提高組 Day1 第一題


def main():
    key = input()
    cypher_text = input()

    key = tuple(map(lambda x: ord(x) - 65, key.upper()))
    plain_text = [''] * len(cypher_text)

    for i in range(len(cypher_text)):
        plain_text[i] = chr((ord(cypher_text[i].upper()) - 65 - key[i % len(key)] + 26) % 26 + 65)
        if cypher_text[i].islower():
            plain_text[i] = plain_text[i].lower()
    
    print(''.join(plain_text))


if __name__ == '__main__':
    main()
