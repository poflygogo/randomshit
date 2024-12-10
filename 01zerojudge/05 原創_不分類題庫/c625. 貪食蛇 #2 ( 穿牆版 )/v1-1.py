# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c625. 貪食蛇 #2 ( 穿牆版 )


class Solution:
    # maxRow = 15, maxCol = 21
    def __init__(self):
        self.map_info = [list(input()) for _ in range(15)]
        self.snake_body = [(0, 0)]
        self.is_dead = False
        self.actions = input().split()
    
    def game_start(self):
        for idx in range(0, len(self.actions), 2):
            for _ in range(int(self.actions[idx + 1])):
                if self.actions[idx] == 'E':
                    if self.snake_body[0][1] == 20:
                        snake_head_temp = (self.snake_body[0][0], 0)
                    else:
                        snake_head_temp = (self.snake_body[0][0], self.snake_body[0][1] + 1)
                elif self.actions[idx] == 'S':
                    if self.snake_body[0][0] == 14:
                        snake_head_temp = (0, self.snake_body[0][1])
                    else:
                        snake_head_temp = (self.snake_body[0][0] + 1, self.snake_body[0][1])
                elif self.actions[idx] == 'W':
                    if self.snake_body[0][1] == 0:
                        snake_head_temp = (self.snake_body[0][0], 20)
                    else:
                        snake_head_temp = (self.snake_body[0][0], self.snake_body[0][1] - 1)
                else: # actions[idx] == 'N'
                    if self.snake_body[0][0] == 0:
                        snake_head_temp = (14, self.snake_body[0][1])
                    else:
                        snake_head_temp = (self.snake_body[0][0] - 1, self.snake_body[0][1])

                if snake_head_temp in self.snake_body[:-1] or \
                    self.map_info[snake_head_temp[0]][snake_head_temp[1]] == 'x':
                    return self.snake_body

                # 食物被吃，除了會增加長度外，也會消耗掉，重複移動到同一個格子不會增加長度
                if self.map_info[snake_head_temp[0]][snake_head_temp[1]] == '$':
                    self.snake_body.insert(0, snake_head_temp)
                    self.map_info[snake_head_temp[0]][snake_head_temp[1]] = 'o'
                else:
                    self.snake_body = [snake_head_temp] + self.snake_body[:-1]
        return self.snake_body


snake = Solution()
print('\n'.join(f'{j} {i}' for i, j in snake.game_start()))
