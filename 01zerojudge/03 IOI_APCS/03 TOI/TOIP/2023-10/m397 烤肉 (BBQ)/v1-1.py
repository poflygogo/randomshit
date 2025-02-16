cost, sticks, item1, item2 = map(int, input().split())

item2_cnt: float = (cost - sticks * item1) / (item2 - item1)
item1_cnt: float = sticks - item2_cnt

if item1_cnt.is_integer() and item2_cnt.is_integer() and item1_cnt >= 0 and item2_cnt >= 0:
    print(f'{item1_cnt: <.0f} {item2_cnt: <.0f}')
else:
    print(-1, -1)
