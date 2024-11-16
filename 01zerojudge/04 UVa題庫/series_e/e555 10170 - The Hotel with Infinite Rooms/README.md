## 解題思路

題目在考等差級數和，公差為 1 ，第一項為 $a_1$，求 D 的值在哪兩項之間

等差數列和公式: $S_n = \frac{(a_1 + a_n)n}{2}$

套用到不等式 $\frac{(a_1 + a_n)n}{2} \le \text{D}$

$\Rightarrow \frac{(a_1 + a_n)(a_n - a_1 + 1)}{2} \le D$

$\Rightarrow (a_1 + a_n)(a_n - a_1 + 1) \le 2D$

$\Rightarrow a_n^2 + a_n + (a_1^2 + a_1 - 2D) \le 0$

$\Rightarrow n >= \frac{-1 + \sqrt{1 - 4(a_1^2 + a_1 - 2D)}}{2}$
