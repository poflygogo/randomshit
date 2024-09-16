from collections import deque

def odd_killer(num_list):
    queue = deque(num_list)
    while len(queue) > 1:
        num = queue.popleft()
        if num % 2 == 0:
            queue.popleft()
        queue.append(num)
    return queue[0]

length = int(input())
num_list = list(map(int, input().split()))

print(odd_killer(num_list))
