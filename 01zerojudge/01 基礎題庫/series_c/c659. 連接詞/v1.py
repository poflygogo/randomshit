data = input().split()
conn = data.pop(0)
print(
    *data,
    sep=f' {conn} '
)