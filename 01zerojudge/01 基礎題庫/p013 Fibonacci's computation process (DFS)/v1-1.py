def fib(n: int):
    print(f"f({n})", end="\n" if n < 2 else " ")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


n = int(input())
print(f"f({n}) = {fib(n)}")
