from math import gcd,ceil


a, b, x, y = map(int, input().split())
if x == 0 or y == 0:
    if b>0 and a<0:
        print(1)
    else:
        print(0)
else:
    x=abs(x)
    y=abs(y)
    l=abs(x*y)//gcd(x,y)
    ans=0
    if a>0 and b>0:
        ans+=(b//x)-ceil(a/x)+1
        ans+=(b//y)-ceil(a/y)+1
        ans-=(b//l)-ceil(a/l)+1
    if b>0 and a<0:
        ans+=(b//x)+abs(a)//x+1
        ans+=(b//y)+abs(a)//y+1
        ans-=(b//l)+abs(a)//l+1
    if a<0 and b<0:
        ans+=(abs(a)//x)-ceil(abs(b)/x)+1
        ans+=(abs(a)//y)-ceil(abs(b)/y)+1
        ans-=(abs(a)//l)-ceil(abs(b)/l)+1
    if a<0 and b==0:
        ans+=(abs(a)//x)+1
        ans+=(abs(a)//y)+1
        ans-=(abs(a)//l)+1
    if a==0 and b>0:
        ans+=(b//x)+1
        ans+=(b//y)+1
        ans-=(b//l)+1
    print(ans)