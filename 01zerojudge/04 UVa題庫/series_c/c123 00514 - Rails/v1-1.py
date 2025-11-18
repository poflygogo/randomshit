# python 3.12
# UVa 00514 Rails
# ZeroJudge c123


def main():
    while n := int(input()):
        while (arr := list(map(int, input().split()))) and arr[0]:
            stack = []
            idx = 0
            for num in range(1, n + 1):  # 模擬從 1 到 n 輸入
                stack.append(num)
                while stack and stack[-1] == arr[idx]:
                    stack.pop()
                    idx += 1
            print("Yes" if len(stack) == 0 else "No")
        print()


main()
