data = input()
code = []
for i in range(len(data) - 1):
    code.append(
        abs(ord(data[i]) - ord(data[i + 1]))
    )
print(
    *code,
    sep=''
)
