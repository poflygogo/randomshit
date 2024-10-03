> 論屎山代碼的危害

題目計分方式
- 每次使用的搜尋次數≤625 50分
- 每次使用的搜尋次數≤75 75分
- 每次使用的搜尋次數≤30 100分


## 解題思路

二分搜
- 若 request(n) == 0，代表 n < answer，下次應該猜更大的數字
- 若 request(n) == 1，代表 n >= answer
  - 這意味著有可能猜中了，或 n > answer，應檢查 n-1

當確認 request(n) == 1 且 request(n - 1) == 0 時，代表找到正確答案了


## 解題紀錄
### v1-1 NA(score: 50%)
```text
#1: 5% TLE (1.5s)
Traceback (most recent call last):
  File "/14701381_g875/code_14701381.py", line 25, in 
    main()
  File "/14701381_g875/code_14701381.py", line 12, in main
    receive = request(mid)
  File "/14701381_g875/code_14701381.py", line 2, in request
    def request(a:int):global st_cnt,st_com;st_cnt +=1;print("request=qwertyuiopasdfghjklzxcvbnm;check=ok;waiting_for_the_answer;next_line=check;reading=false;check_point=false")if st_com else print("",end="");    return a>=int(st_ans2-st_ans1) if  1 else  0
OSError: [Errno 27] File too large
Exception ignored in: <_io.TextIOWrapper name='' mode='w' encoding='utf-8'>
OSError: [Errno 27] File too large
```
> 三小? 出現沒見過的 Error

### v1-2 NA(score: 75%)
- 修改遍歷方式
```text
答案正確，但搜尋次數過多。
您的答案為：30960
正確答案為：30960
```

### v1-3 NA(score:45%)

### v1-4 NA(score:60%)

### v1-5 AC(19ms, 3.4MB)
