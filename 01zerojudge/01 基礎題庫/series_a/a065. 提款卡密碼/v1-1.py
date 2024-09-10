code = input()
password = ''
length = len(code)
code_ascii = tuple(ord(i) for i in code)
for i in range(length-1):
    password += str(abs(code_ascii[i+1]-code_ascii[i]))
print(password)
