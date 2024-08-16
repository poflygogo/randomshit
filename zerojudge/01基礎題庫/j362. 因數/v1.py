output = []
num = int(input())

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        output.extend((i, num//i))

if input() == "no":
    del output[0]

print(output)
output.sort()
print(output)

print(
    *output,
    f"{num}的因數個數是{len(output)}，{num}的因數總和是{sum(output)}",
    sep="\n"
)
