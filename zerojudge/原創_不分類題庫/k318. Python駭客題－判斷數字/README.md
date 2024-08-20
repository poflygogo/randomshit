## 題目
給兩個函數，分別是 Alice 寫的和 Bob 寫的，但其中一個人寫的是錯的，請輸出正確的函數，並輸出當輸入的值為什麼時，會導致錯誤。

> 數字的定義: 必須要是 0123456789 構成的十進位阿拉伯數字，且不為空白。

#### Alice的答案:
```py
def isNumber(s: str) -> bool:
    return s.isdecimal()
```
#### Bob的答案:
```python
def isNumber(s: str) -> bool:
    return s != '' and all(48 <= c <= 57 for c in map(ord, s))
```
#### 輸出的範例格式:
```python
Alice
1234567890
```

具體來說, 用 python 應該這樣輸入
```python
print('Alice\n1234567890', end='')
```
而不是這樣
```py
print('Alice')
print('1234567890')
```

他們輸出的內容是不一樣的


## 解析
可以確定的是 Alice 的答案是錯誤的，Bob 才是正確的

Bob 直接判斷每個字元的 ASCII 編碼，如果編碼介於 48 到 57 之間的就是數字，而查看表格後確實是如此。

Alice 使用內建函數`isdecimal()`判斷，`isdecimal()`會判斷輸入的`string`是否為十進位數字，若為真則返回`True`，反之則返回`False`

然而對`isdecimal()`來說，並非只有 0123456789 這些阿拉伯數字才是十進位數字，以下是會被`isdecimal()`的字元列表:

```python
"0123456789"  DIGIT ZERO~NINE
"٠١٢٣٤٥٦٧٨٩"  ARABIC-INDIC DIGIT ZERO~NINE
"०१२३४५६७८९"  DEVANAGARI DIGIT ZERO~NINE
"০১২৩৪৫৬৭৮৯"  BENGALI DIGIT ZERO~NINE
"੦੧੨੩੪੫੬੭੮੯"  GURMUKHI DIGIT ZERO~NINE
"૦૧૨૩૪૫૬૭૮૯"  GUJARATI DIGIT ZERO~NINE
"୦୧୨୩୪୫୬୭୮୯"  ORIYA DIGIT ZERO~NINE
"௦௧௨௩௪௫௬௭௮௯"  TAMIL DIGIT ZERO~NINE
"౦౧౨౩౪౫౬౭౮౯"  TELUGU DIGIT ZERO~NINE
"೦೧೨೩೪೫೬೭೮೯"  KANNADA DIGIT ZERO~NINE
"൦൧൨൩൪൫൬൭൮൯"  MALAYALAM DIGIT ZERO~NINE
"๐๑๒๓๔๕๖๗๘๙"  THAI DIGIT ZERO~NINE
"໐໑໒໓໔໕໖໗໘໙"  LAO DIGIT ZERO~NINE
"༠༡༢༣༤༥༦༧༨༩"  TIBETAN DIGIT ZERO~NINE
"၀၁၂၃၄၅၆၇၈၉"  MYANMAR DIGIT ZERO~NINE
"០១២៣៤៥៦៧៨៩"  KHMER DIGIT ZERO~NINE
"０１２３４５６７８９"  FULLWIDTH DIGIT ZERO~NINE
"𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"  MATHEMATICAL BOLD DIGIT ZERO~NINE
"𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"  MATHEMATICAL DOUBLE-STRUCK DIGIT ZERO~NINE
"𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"  MATHEMATICAL SANS-SERIF DIGIT ZERO~NINE
"𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"  MATHEMATICAL SANS-SERIF BOLD DIGIT ZERO~NINE
"𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"  MATHEMATICAL MONOSPACE DIGIT ZERO~NINE
```

## 產生符合題目要求的字元列表的python程式碼
```python
def isNumberA(s: str) -> bool:
    return s.isdecimal()
def isNumberB(s: str) -> bool:
    return s != '' and all(48 <= c <= 57 for c in map(ord, s))
t=0
print("以下字元會出現不一樣的結果:")
for s in range(0, 65535):
    if(isNumberA(chr(s))!=isNumberB(chr(s))):
        t=t+1
        print(chr(s))
print("總共",t,"個字元符合題目要求")

# zerojudge k318. Python駭客題－判斷數字
# d2513850
```


## 參考資料
- [What's the difference between str.isdigit(), isnumeric() and isdecimal() in Python?](https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth) | [Stack Overflow](https://stackoverflow.com/) 2017-07-03 [2024-08-20]

- [Python String isdecimal()](https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/isdecimal/python-string-isdecimal/) | [toppr](https://www.toppr.com/ask/) 2024-08-20 [2024-08-20]

- [ASCII Table](https://www.asciitable.com/) 2024-08-20 [2024-08-20]

- [内置类型 — Python 3.12.5 文档](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.isdecimal) | [python.org](https://www.python.org/) 2024-08-20 [2024-08-20]

- [產生符合題目要求的字元列表的python程式碼](https://gist.github.com/d2513850/ad068b8881ed547ac77a9789b9e53e28) | gist 2024-08-13 [2024-08-20]