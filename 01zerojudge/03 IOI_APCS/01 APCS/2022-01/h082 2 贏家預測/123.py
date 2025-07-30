n,m=map(int,input().split())
att=[0]+list(map(int,input().split()))#戰力
res=[0]+list(map(int,input().split()))#應變力
peoples=list(map(int,input().split()))#順序
losetimes=[0]*(n+1)

while len(peoples)>1:
    win,lose=[],[]
    for i in range(0,len(peoples)-1,2):
        first,second=peoples[i],peoples[i+1]# 比較
        a,b,c,d=att[first],res[first],att[second],res[second]
        
        if a*b>=c*d:
            if losetimes[second]<m-1:lose.append(second)
            att[second]+=(c//2)
            res[second]+=(d//2)
            losetimes[second]+=1
            att[first]+=c*d//(2*b)
            res[first]+=c*d//(2*a)
            win.append(first)
        else:
            if losetimes[first]<m-1:lose.append(first)
            att[first]+=a//2
            res[first]+=b//2
            losetimes[first]+=1
            att[second]+=a*b//(2*d)
            res[second]+=a*b//(2*c)
            win.append(second)

    if len(peoples)%2==1:
        win.append(peoples[-1])
    peoples=win+lose

print(peoples[0])
