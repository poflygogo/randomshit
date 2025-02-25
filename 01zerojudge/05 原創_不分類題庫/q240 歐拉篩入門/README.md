# 題目敘述

參考連結:https://hackmd.io/@EricOWO/Skd4K9tXs
 
建立一個整數n，將其值設為範圍上限
將is_prime[]中所有元素設為1 #如果is_prime[n]==1，代表n是質數 
建立一個存質數的primelist   #將目前已知的所有質數存於primelist中
```
for i = 2 ~ n :
    if is_prime[i] == 1 :   #如果is_prime[i]==1，將i加入primelist
        將i加入primelist中
    for j = primelist中的元素 :
        if i * j > n :     #如果i*j超出範圍，跳出迴圈
            跳出for迴圈
        isprime[i * j] = 0 #將i*j標記為合數
        if i % j == 0 :
            跳出for迴圈   #歐拉篩法關鍵：如果i是j的倍數，則i有質因數j，
                          #且primelist中元素只會越來越大，所以到這裡就
                          #需停下(因為每個合數只能被自身最小的質因數篩
                          #選過一遍)
```

Q.個人對於if(i%j==0)的解釋不理解，進行逐一模擬一次

```
2 is T
>>push 2
2*2=F
 
3 is T
>>push 2,3
3*2=F
3*3=F
 
4 is F
4*2=F
4%2==0//!!!4*3=F未執行
>>break
 
5 is T
>>push 2,3,5
5*2=F
5*3=F
5*5=F
 
6 is F
6*2=F
6%2==0//!!!6*3=F 6*5=F未執行
>>break
 
7 is T
>>push 2,3,5,7
7*2=F
7*3=F
7*5=F
7*7=F
 
8 is F
8*2=F
8%2==0//!!!8*3==F 8*5==F 8*7==F未執行
>>break
 
9 is F
9*2=F
9*3=F
9%3==0//!!!9*5=F 9*7=F未執行
>>break
 
10 is F
10*2=F
10%2==0//!!!10*3=F 10*5=F 10*7=F未執行
>>break
```

如果去除if(i%j==0)那行，則!!!處皆會執行，但如6*3=F 6*5=F這兩行會被之後的9*2=F 15*2=F代為執行，所以屬於冗贅的執行。
 
Extra：
如果將if(i%j==0)替換為if(isprime[i]==F)或是if(!isprime[i])，則如果i值在更早就被判定為非質數，除了i*2=F以外將不再刪去其他數值，這將造成 非質數*3 非質數*5...將不被刪去，結果上此行使數值範圍1~1e6的質數表數量由78498變成250459直接出錯，當x為大於2的質數，則x的倍數在超過x*x之後，若不是2的倍數，將不被刪去，27 45 63等數字都會跑出來。
 
實作模板
```cpp
#include <iostream>
#include <vector>
using namespace std;
//歐拉篩
int ccount=0;
vector<int> CalcuPrime(long long num)
{
    vector<int> yesPrime;
    vector<bool> isPrime( num+5, true);
    isPrime[0]=isPrime[1]=false;
    for(int i=2;i<=num;i++){
        if(isPrime[i]){
            yesPrime.push_back(i);
            ccount++;
        }
        for(auto j : yesPrime){
            if( i*j > num) break;
            isPrime[ i*j ] = false;
    if(i%j==0) break;
            //if(!isPrime[i]) break;//替換此行質數表刪不掉27,45,63...
        }
    }
    return yesPrime;
}
 
int main(void)
{
    auto Prime = CalcuPrime( 1e6 );
    cout<<ccount<<'\n';
    for(auto i : Prime){
        cout<<i<<'\n';
    }
 
    return 0;
}
```

## 輸入說明

多行測資以EOF結束，一行一個整數(範圍在int16內)，所有質數總和為M，非質數總和為N。

## 輸出說明

請輸出M和N，中間以一個空格相隔。

## 範例輸入 #1

0
1
2
3
4

## 範例輸出 #1

5 5

## 範例輸入 #2

-1
-2
-3
0
1
2
3

## 範例輸出 #2

5 -5
