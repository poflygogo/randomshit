## 解題紀錄
### v1-1 WA(line:62)
```
您的答案為: Yes
正確答案為: No
```
- 檢查 bytes.__str__ 的內容

### v1-2 WA(line:62)
- 不再調用 bytes.__str__ ，改用 bytes.hex()

### v1-3 AC(21ms, 4.2MB)
- 當輸入的字元非中文字元時就輸出 no