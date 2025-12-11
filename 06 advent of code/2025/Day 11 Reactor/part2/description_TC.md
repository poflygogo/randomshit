# --- 第二部分 ---

部分感謝您的分析，精靈們對問題有了一些了解。他們現在知道有問題的資料路徑同時經過了 `dac`（一個[數位類比轉換器](https://zh.wikipedia.org/wiki/數位類比轉換器)）和 `fft`（一個執行[快速傅立葉變換](https://zh.wikipedia.org/wiki/快速傅立葉變換)的設備）。

他們仍然不確定具體是哪條路徑出了問題，所以他們現在需要您找出從 `svr`（伺服器機櫃）到 `out` 的每一條路徑。然而，您找到的路徑必須同時經過 `dac` 和 `fft`（順序不拘）。

例如：

```text
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
```

這份新的設備清單包含許多從 `svr` 到 `out` 的路徑：

```text
svr,aaa,fft,ccc,ddd,hub,fff,ggg,out
svr,aaa,fft,ccc,ddd,hub,fff,hhh,out
svr,aaa,fft,ccc,eee,dac,fff,ggg,out
svr,aaa,fft,ccc,eee,dac,fff,hhh,out
svr,bbb,tty,ccc,ddd,hub,fff,ggg,out
svr,bbb,tty,ccc,ddd,hub,fff,hhh,out
svr,bbb,tty,ccc,eee,dac,fff,ggg,out
svr,bbb,tty,ccc,eee,dac,fff,hhh,out
```

然而，在從 `svr` 到 `out` 的路徑中，只有 `2` 條同時經過了 `dac` 和 `fft`。

找出所有從 `svr` 到 `out` 的路徑。**其中有多少條路徑同時經過了 `dac` 和 `fft`？**
