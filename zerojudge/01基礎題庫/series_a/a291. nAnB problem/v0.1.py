"""
WA
注意重複元素
"""

while True:
    try:
        answer = tuple(input().split())
        for _ in range(int(input())):
            test = tuple(input().split())
            p = 0
            q = 0
            for num in range(len(test)):
                if test[num] == answer[num]: p += 1
                elif test[num] in answer: q += 1
            print(f"{p}A{q}B")
    except:break
