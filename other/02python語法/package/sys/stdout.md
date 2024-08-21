# sys.stdout
stdout (standard output) 是標準輸出流的簡稱。簡單來說，它就是一個預設的通道，程式可以透過這個通道將訊息輸出到外部。

## 作用
- 顯示程式執行結果： 大部分程式會將計算結果、提示訊息等資訊輸出到 stdout，以便使用者查看。
- 將資料傳遞給其他程式： stdout 的輸出可以被其他程式作為輸入，實現程式的串聯。

## 特性
- 預設輸出目的地： 通常，stdout 的輸出會直接顯示在終端（terminal）或命令提示符（command prompt）上。
- 可重定向： 可以使用重定向符號（如 > 或 >>）將 stdout 的輸出重定向到文件。
- 可管道化： 可以將一個程式的 stdout 作為另一個程式的 stdin，實現管道操作。

## 和 stderr , print() 的區別
stdout： 用於輸出一般的資訊，例如程式執行結果、提示訊息等。
stderr： 用於輸出錯誤訊息。
print(): 用於輸出一般的資訊

在更底層的地方，print() 其實是把函數的傳入值輸出到 stdout

## 常用方法
- sys.stdout.write(): 和 print() 類似，但只接受字符串 string，需要自己輸出換行符 \n