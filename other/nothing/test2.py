import sys

def count(a, b, op): #a: int, b: int, c: str
    
    if (op=='+'):
        return a+b
    
    if (op=='-'):
        return a-b  
    if (op=='*'):
        return a*b
        
    if (op=='/'):
        return a//b #題目有說除法不要留小數
        
    if (op=='%'):
        return a%b
    
    return -999

def calculate(expr): #expr: str
    
    exprs = expr.split() #把每個數字, 號分開來
    opers = [] #裝str
    nums = [] #裝int
    
    prior = {'+':1, '-':1, '*':2, '/':2, '%':2, '(':-1}
    
    for ele in exprs:
        
        if ele=='(':
            opers.append('(')
            
        elif ele==')':
            
            #算到左括號為止，照理講括號裡面會只剩下+-，頂多最後面(opers最前面)有一個*/%
            while opers[-1] != '(': 
                
                #注意順序, nums的最前面會是比較晚加入的數字，也就是是計算時的第二個數字
                val2 = nums.pop(); val1 = nums.pop(); 
                op = opers.pop()
                
                result = count(val1, val2, op)
                nums.append(result)
            
            opers.pop() #pop掉'('
                
        elif ( ele in ['+', '-', '*', '/', '%'] ):
            
            while (opers and prior[ele]<=prior[opers[-1]]):
                
                #注意順序
                val2 = nums.pop(); val1 = nums.pop(); 
                op = opers.pop()
                
                result = count(val1, val2, op)
                nums.append(result)
            
            opers.append(ele)
            
        else: #ele是數字
            nums.append( int(ele) )
            
        
    while (opers): #把剩下的清掉，一樣，照理來講opers裡面會只剩下+-，頂多最前面有一個*/%
       
        val2 = nums.pop(); val1 = nums.pop(); #注意順序
        op = opers.pop()
                
        result = count(val1, val2, op)
        nums.append(result)
    
    #這個時候，opers應該要是空的, nums剩下一個數字，就是答案
    return nums[-1]

for inp in sys.stdin:
    
    ans = calculate(inp)
    print(ans)