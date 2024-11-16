# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11995 I Can Guess the Data Structure!
# ZeroJudge e548


while True:
    try:
        n = int(input())

    except EOFError:
        exit()

    else:
        is_stack = True
        is_queue = True
        is_priority_queue = True

        items = []
        for _ in range(n):
            command, item = map(int, input().split())
            if command == 1:
                items.append(item)
            
            # 若所有 flag 都是 False，則毋須繼續後續判斷，代表數據結構不在 stack, queue, priority queue 的範圍內
            elif any((is_stack, is_queue, is_priority_queue)):

                # 若取出的物件不在 list 內，代表所有條件都不符合
                if item not in items:
                    is_stack = False
                    is_queue = False
                    is_priority_queue = False
                    continue
                
                if is_stack and item != items[-1]:
                    is_stack = False
                
                if is_queue and item != items[0]:
                    is_queue = False
                
                # 根據題意，priority queue 會優先取出最大值
                if is_priority_queue and item != max(items):
                    is_priority_queue = False
                
                items.remove(item)
        
        print(
            'stack' if (is_stack, is_queue, is_priority_queue) == (True, False, False) else
            'queue' if (is_stack, is_queue, is_priority_queue) == (False, True, False) else
            'priority queue' if (is_stack, is_queue, is_priority_queue) == (False, False, True) else
            'not sure' if any((is_stack, is_queue, is_priority_queue)) else
            'impossible'
        )
