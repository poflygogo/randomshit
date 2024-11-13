from sys import stdin


numbers = [int(stdin.readline().rstrip())]
length = 1
print(numbers[0])
for num in stdin:
    num = int(num.rstrip())

    # 二分搜尋找插入的位置
    lft, rgt = 0, length
    while lft < rgt:
        mid = (lft + rgt) // 2
        if numbers[mid] < num:
            lft = mid + 1
        else:
            rgt = mid
    numbers.insert(lft, num)

    length += 1
    if length % 2 == 0:
        a = length // 2
        print(sum(numbers[a - 1: a + 1]) // 2)
    else:
        print(numbers[length // 2])
