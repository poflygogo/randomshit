# itertools.combinations() 與 itertools.permutations()

專門用於生成序列的排列。它可以從一個給定的可迭代對象中，取出指定長度的元素的所有排列組合。

## 基本語法
```python
import itertools

itertools.combinations(iterable, r)
itertools.permutations(iterable, r)
```
其中:
- iterable : 一個可迭代對象，如列表、字符串等，表示要進行排列的元素集合。
- r : 可選，整數，表示每次取出的元素個數，默認取所有元素進行全排列。

## 功能與比較

||`combinations`|`permutations`|
|:-:|:-|:-|
|功能|生成所有可能的排列組合，每個排列組合都是一個元組|生成所有可能的排列組合，每個排列組合都是一個元組|
|重複元素| 每個排列組合中的元素都是唯一的，不會出現重複<br>**考慮元素的順序**，即 AB 和 BA 是不同的排列| 每個排列組合中的元素都是唯一的，不會出現重複<br>**不考慮元素的順序**，即 AB 和 BA 被視為相同的組合|
|有序|排列組合是按照字典序生成的|排列組合是按照字典序生成的|

## 應用場景
- 全排列問題： 許多算法問題需要生成所有可能的排列，例如：
    - 破解密碼
    - 找尋最優解
    - 產生隨機序列
- 組合數學： 在組合數學中，排列是基礎概念之一。
- 遊戲開發： 在遊戲開發中，可以用來生成各種排列組合，例如洗牌、生成隨機地圖等。

## 習題
- [i645. 排列組合-組合](https://zerojudge.tw/ShowProblem?problemid=i645) | [Zero Judge](https://zerojudge.tw/)
- [e446. 排列生成](https://zerojudge.tw/ShowProblem?problemid=e446) | [Zero Judge](https://zerojudge.tw/)
- [a524. 手機之謎](https://zerojudge.tw/ShowProblem?problemid=a524) | [Zero Judge](https://zerojudge.tw/)

## 參考資料
- [itertools — Functions creating iterators for efficient looping](https://docs.python.org/3.12/library/itertools.html#itertools.combinations) | [Python 3.12.5 documentation](https://docs.python.org/3.12/) 2024-08-22 [2024-08-22]

- [高效迭代器 itertools](https://steam.oxxostudio.tw/category/python/library/itertools.html#a16) | [Python 教學](https://steam.oxxostudio.tw/category/python/index.html) | [STEAM 教育學習網](https://steam.oxxostudio.tw/) 2024-08-22 [2024-08-22]