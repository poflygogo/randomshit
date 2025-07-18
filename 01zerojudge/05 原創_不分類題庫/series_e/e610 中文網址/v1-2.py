# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e610. 中文網址


from typing import ByteString
from string import hexdigits
import re


def unquote_impl(string, hextobyte=None, hexdig=hexdigits):
    # 保證 string 必定是 bytes 物件
    if isinstance(string, str):
        string = string.encode("utf-8")

    # 將 string 根據 % 的位置分割成串列
    # 若長度為 1，代表 % 不存在，直接返回
    bits = string.split(b"%")
    if len(bits) == 1:
        return string
    
    # 創建 bytearray 物件，作用相當於 list[bytes]
    res = bytearray(bits[0])
    append = res.extend

    # 預處理 bytes 物件與數值的對應關係，這樣就不用每次都重新計算
    if hextobyte is None:
        hextobyte = {
            (a + b).encode(): bytes.fromhex(a + b) for a in hexdig for b in hexdig
        }

    for item in bits[1:]:
        try:
            append(hextobyte[item[:2]])
            append(item[2:])
        except KeyError:
            append(b"%")
            append(item)
    return res


# 創建一個 re.compile 物件，有助於提升執行效率
asciire = re.compile("([\x00-\x7f]+)")


def generate_unquoted_parts(string: str, encoding: str = "utf-8"):
    previous_match_end = 0
    for ascii_match in asciire.finditer(string):
        start, end = ascii_match.span()
        yield string[previous_match_end:start]
        yield unquote_impl(ascii_match[1]).decode(encoding)
        previous_match_end = end
    yield string[previous_match_end:]


while True:
    try:
        url = input()
        print(''.join(i for i in generate_unquoted_parts(url)))
    except EOFError:
        break
