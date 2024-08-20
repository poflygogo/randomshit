## 題目
實作一個函數`isAscendingSequence(n)`，其輸入參數`n`為一個僅包含整數(`int`)的列表(`list`)，該函數需要回傳一個布林值(`bool`)用以判斷整數列表`n`是否為「**遞增數列**」？若一個整數列表至少包含一個整數，且對於所有整數皆大於其前一項（如果存在的話）的整數，則我們稱該整數列表為「**遞增數列**」。

有鑑於上一次的經驗，Alice 和 Bob 這次決定先核對彼此所撰寫的函數是否會有相同的回傳值，他們將由 Alice 所完成的函數重新命名為`isAscendingSequenceAlice(n)`，而由 Bob 所完成的函數則是重新命名為`isAscendingSequenceBob(n)`，並且共同撰寫另一個函數`checkReturnValuesAreSame(n)`用以判斷對於輸入參數`n`來說兩者是否有相同的回傳值。

```python
from typing import List

# Alice version
def isAscendingSequenceAlice(n: List[int]) -> bool:
    if not n:
        return False
    for i in range(1, len(n)):
        if n[i-1] >= n[i]:
            return False
    return True

# Bob version
def isAscendingSequenceBob(n: List[int]) -> bool:
    return n and all(a < b for a, b in zip(n, n[1:]))

# Checks if two functions have the same return value
def checkReturnValuesAreSame(n: List[int]) -> bool:
    return isAscendingSequenceAlice(n) == isAscendingSequenceBob(n)
```

## 解析

目前還沒想好答案

## 參考資料

笑死，我根本還沒動手