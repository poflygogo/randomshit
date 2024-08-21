## 解題思路

這題對python來說，考驗的是如何使用轉譯字符，有很多方式能處理

- 如果想把用*單引號*包起來的字串印出*單引號*，要對裡面的*單引號*前方添加轉意字符`\`
- 如果想把用*雙引號*包起來的字串印出*雙引號*，要對裡面的*雙引號*前方添加轉意字符`\`

```py
str_1 = 'my name is "Bob", i love \'baseball\''
str_2 = "my name is \"Bob\", i love 'baseball'"
```
也可以使用 row string 的功能，在字串前方添加 `r'something'`, `r"something"`，特別是你想印`\`出來時

```py
str_1 = r"C:\Users\John\Documents"
```


## 解題紀錄
### v1 	WA(line:1)
```txt
您的答案為: 'C' can use printf('%d',n); to show integer like 1252
正確答案為: 'C' can use printf("%d",n); to show integer like 1252
```
雙引號vs單引號 (╯°□°）╯︵ ┻━┻

### v2 (18ms, 3.2MB)
- 使用轉意字符`\`處理`%d`