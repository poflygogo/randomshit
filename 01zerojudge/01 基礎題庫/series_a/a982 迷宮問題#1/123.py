from collections import deque

def bfs(maze, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
   
    start = (1, 1)
    end = (n-2, n-2)
   
    queue = deque([(start, 1)])  
    visited = [[False] * n for _ in range(n)]
    visited[1][1] = True
   
    while queue:
        (x, y), dist = queue.popleft()
       
        if (x, y) == end:
            return dist
       
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
           
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append(((nx, ny), dist + 1))
   
    return "No solution!"

n = int(input())
maze = [input().strip() for _ in range(n)]

result = bfs(maze, n)
print(result)