UVa 10219

## 解題紀錄
### v1-1 AC(0.9s, 58.7MB)

### v1-2 AC(0.9s, 3.3MB)
- 將**列表生成式**替換成**生成器表達式**

### v1-3 TLE
- 調整計算 b 的方式

### v2-1 RE(code:1)
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14588370_b897/code_14588370.py", line 14, in 
    int(math.log(math.comb(a, b), 10)) + 1
AttributeError: module 'math' has no attribute 'comb'
```
- 使用 math.comb 計算 C(a, b) 的值
> 靠邀阿 zerojudge 的 python 版本沒有這個

### v3-1 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14588402_b897/code_14588402.py", line 17, in 
    (int(math.sqrt(2 * b * math.pi) * (b / math.e) ** b) + 1) /
OverflowError: (34, 'Numerical result out of range')
```
- 使用斯特林公式計算
> 笑死，溢位了，原來 python 處理數字也不是無敵的<br>
> 不曉得其他使用 python 的人是怎麼處理溢位的

### v3-2 TLE
- 無論如何，盡可能避免浮點數
  - 將 e 設定位 3
  - 小數點一律無條件捨去到整數位
> 沒有溢位了，但TLE......<br>
> 冪運算很耗時，是嗎?
