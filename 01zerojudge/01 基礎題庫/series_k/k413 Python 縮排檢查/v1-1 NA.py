# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k413. Python 縮排檢查


def indent_checker(text: str, expect: list, next_indent: bool):
    indent = len(text) - len(text.lstrip())
    # 該縮進時不縮進
    if next_indent is True and indent == (expect[-1] if expect else 0):
        raise IndentationError('expected an indented block')
    
    # 不該縮進時縮進
    if next_indent is False and indent > (expect[-1] if expect else 0):
        raise IndentationError('unexpected indent')
    
    if next_indent is False and indent < (expect[-1] if expect else 0):
        # 未與任何區塊對齊
        if indent > 0 and indent not in expect:
            raise IndentationError('unindent does not match any outer indentation level')
        elif indent == 0:
            expect.clear()
        else:
            del expect[-expect[::-1].index(indent) - 1:]
    
    if next_indent is True:
        expect.append(indent)

    return text[-1] == ':'


def main():
    expect = []             # 紀錄每個區塊縮進的格數
    next_indent = False     # 是否縮進
    count = 1               # 紀錄程式碼行數
    while True:
        try:
            text = input()
            next_indent = indent_checker(text, expect, next_indent)
            count += 1

        except EOFError:
            print('Indention OK')
            break

        except IndentationError as e:
            print(f'line {count}', text, e, sep='\n')
            break


if __name__ == '__main__':
    main()
