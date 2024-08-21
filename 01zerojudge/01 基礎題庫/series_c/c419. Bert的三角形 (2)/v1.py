num = int(input())
for i in range(num):
    print(f"{'_' * (num - i - 1)}{'*' * (i + 1)}")