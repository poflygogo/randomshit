import time

def timeit(func, *args, **kwargs):
    start = time.perf_counter()
    for _ in range(1000000):
        func(*args, **kwargs)
    end = time.perf_counter()
    return end - start

num = 123456789

# 使用 bin()
t1 = timeit(bin, num)
print(f"bin() took {t1:.6f} seconds")

# 使用 format()
t2 = timeit(lambda: format(num, 'b'))
print(f"format() took {t2:.6f} seconds")