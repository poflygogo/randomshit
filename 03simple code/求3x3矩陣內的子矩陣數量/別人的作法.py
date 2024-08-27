def count_blocks(matrix):
    def dfs(matrix, visited, i, j):
        # If out of bounds or already visited or not a block, return
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or visited[i][j] or matrix[i][j] == 0:
            return
        # Mark the current cell as visited
        visited[i][j] = True
        # Explore all 4 possible directions (up, down, left, right)
        dfs(matrix, visited, i - 1, j)
        dfs(matrix, visited, i + 1, j)
        dfs(matrix, visited, i, j - 1)
        dfs(matrix, visited, i, j + 1)

    if not matrix:
        return 0
    
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    block_count = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and not visited[i][j]:
                # Start a new block search
                dfs(matrix, visited, i, j)
                block_count += 1
    
    return block_count

# Example usage
matrix = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

print(count_blocks(matrix))  # Output should be 2