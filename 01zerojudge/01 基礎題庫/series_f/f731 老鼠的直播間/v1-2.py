in_time, ex_time = [], []
for _ in range(int(input())):
    a, b = map(int, input().split())
    in_time.append(a)
    ex_time.append(b)

in_time.sort()
ex_time.sort()

viewer = 0
viewer_flow = []
idx = 0
for i in in_time:
    viewer += 1
    while ex_time[idx] < i:
        viewer -= 1
        idx += 1
    viewer_flow.append(viewer)
print(max(viewer_flow))
