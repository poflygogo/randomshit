# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k413. Python 縮排檢查


def indent_checker(text: str, expect: list, next_indent: bool):
    indent = len(text) - len(text.lstrip())
    # 該縮進時不縮進
    if next_indent:
        if indent == (expect[-1] if expect else 0):
            raise IndentationError('expected an indented block')
        else:
            expect.append(indent)
    
    # 不該縮進時縮進
    elif indent > (expect[-1] if expect else 0):
        raise IndentationError('unexpected indent')
    
    # 檢查是否有結束程式碼區塊的行為
    elif indent < (expect[-1] if expect else 0):

        # 找不到匹配的程式碼區塊
        if indent > 0 and indent not in expect:
            raise IndentationError('unindent does not match any outer indentation level')
        
        elif indent == 0:
            expect.clear()

        else:
            del expect[expect.index(indent) + 1:]
        
    return text[-1] == ':'


def main():
    expect = []             # 紀錄每個區塊縮進的格數(其實是當成stack在用)
    next_indent = False     # 是否縮進
    count = 1               # 紀錄程式碼行數
    while True:
        try:
            text = input().rstrip()
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
