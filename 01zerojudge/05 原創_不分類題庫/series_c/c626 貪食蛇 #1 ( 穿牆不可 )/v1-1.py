# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c626. 貪食蛇 #1 ( 穿牆不可 )


class Solution:
    # maxRow = 15, maxCol = 21
    def __init__(self):
        self.map_info = [input() for _ in range(15)]
        self.snake_body = [(0, 0)]
        self.is_dead = False
        self.actions = input().split()
    
    def game_start(self):
        for idx in range(0, len(self.actions), 2):
            for _ in range(int(self.actions[idx + 1])):
                if self.actions[idx] == 'E':
                    snake_head_temp = (self.snake_body[0][0] + 1, self.snake_body[0][1])
                elif self.actions[idx] == 'S':
                    snake_head_temp = (self.snake_body[0][0], self.snake_body[0][1] + 1)
                elif self.actions[idx] == 'W':
                    snake_head_temp = (self.snake_body[0][0] - 1, self.snake_body[0][1])
                else: # actions[idx] == 'N'
                    snake_head_temp = (self.snake_body[0][0], self.snake_body[0][1] - 1)

                if snake_head_temp in self.snake_body[:-1] or \
                    not 0 <= snake_head_temp[0] < 15 or \
                    not 0 <= snake_head_temp[1] < 21 or \
                    self.map_info[snake_head_temp[0]][snake_head_temp[1]] == 'x':
                    return self.snake_body

                if self.map_info[snake_head_temp[1]][snake_head_temp[0]] == '$':
                    self.snake_body.insert(0, snake_head_temp)
                else:
                    self.snake_body = [snake_head_temp] + self.snake_body[:-1]
        return self.snake_body


snake = Solution()
print('\n'.join(f'{i} {j}' for i, j in snake.game_start()))
