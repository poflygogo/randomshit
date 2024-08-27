import string

def infixToPostfix(infixexpr):

    prec = {
    '+':1, '-':1, '*':2,
    '/':2, '(':3, ')':0}

    opStack = []
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:

        if token in string.ascii_uppercase:#数字
            postfixList.append(token)

        elif token == '(':#左括号入栈
            opStack.append(token)

        elif token == ')':#右括号
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
            
        else:
            while opStack and \
                      (prec[opStack[-1]] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.append(token)
            
    while opStack:
        postfixList.append(opStack.pop())
    return ' '.join(postfixList)

s = input()
print(infixToPostfix(s))