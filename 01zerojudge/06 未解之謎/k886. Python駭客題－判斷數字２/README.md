## 題目
題目提供兩個函數，分別是 Carol 和 Dave 寫的，但其中一個人寫的是錯的，請輸出正確的一方，並輸出當輸入的值為什麼時，會導致錯誤。

###函數功能要求:
實做一個函數`isNumber(s)`，其輸入參數`s`為一個字串(`str`)，該函數需要回傳一個布林值(`bool`)用以判斷字串`s`是否為「數字」？

> 若一個字串至少包含一個字元，且之中的每個字元皆為阿拉伯數字`0123456789`其中之一，則我們稱該字串為「數字」。

### Carol的函數
```python
import re

def isNumber(s: str) -> bool:
    return re.match(r'^\d+$', s, re.A) is not None
```

### Dave的函數
```python
from string import digits

def isNumber(s: str) -> bool:
    return bool(s) and all(c in digits for c in s)
```

## 輸出的範例格式
```python
Carol
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

## 解題思路

我不知道 `re.match` 和 `string.digit` 是幹嘛的，給我一點時間google......但我感覺和先前的題目有關，八成又是什麼unicode編碼在搞

Carol 的那個是**正則表達式**嗎? 我還沒學會QQ

還有，觀這作題風格，其實就是 Alice 和 Bob 吧!你們改名了嗎!?

特別是那個`all()`，這麼喜歡`all()`的人肯定就是 Bob 了

## 參考資料

None