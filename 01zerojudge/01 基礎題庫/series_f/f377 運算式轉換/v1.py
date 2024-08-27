from sys import stdin, stdout

weight = {
    '+':1, '-':1, '*':2,
    '/':2, '(':3, ')':0
}

for line in stdin:
    line = line.strip().split()

    result, stack = [], []
    for item in line:

        if item in ('+', '-', '*', '/', '(', ')'):
            while stack and weight[item] <= weight[stack[-1]]:
                if item == ')':
                    i = stack.pop()
                    if i != '(':
                        result.append(i)
                    else:
                        break
                else:
                    if stack[-1] == '(':
                        stack.append(item)
                        break
                    else:
                        result.append(stack.pop())
            else:
                if item != ')':
                    stack.append(item)
        else:
            result.append(item)
    
    result.extend(stack[::-1])

    stdout.write(f'{" ".join(result)}\n')