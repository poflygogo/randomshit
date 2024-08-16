output = []
num = int(input())

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        output.extend((i, num//i))

output.sort()

if input() == "no":
    del output[0]
    del output[-1]

print(*output, f"{num}的因數的個數是{len(output)}，{num}的因數的總和是{sum(output)}", sep="\n")
