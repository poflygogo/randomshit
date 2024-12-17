# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11483 Code Creator
# ZeroJudge j061


def main():
    cases = 0
    while True:
        n = int(input())
        if n == 0:
            break
        cases += 1
        text = [input() for _ in range(n)]
        print(
            f'Case {cases}:',
            '#include<string.h>',
            '#include<stdio.h>',
            'int main()',
            '{',
            *[f'printf("{line}\\n");' for line in format_as_C(n, text)],
            'printf("\\n");',
            'return 0;',
            '}',
            sep='\n'
        )


def format_as_C(n: int, text: list) -> list:
    for i in range(n):
        if '\\' in text[i]:
            text[i] = text[i].replace('\\', '\\\\')
        if '"' in text[i]:
            text[i] = text[i].replace('"', '\\"')
    return text


main()
