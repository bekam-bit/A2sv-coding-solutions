class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < rows and 0 <= col < cols)
        
        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            for dr, dc in dir:
                new_row, new_col = row + dr, col + dc
                dfs(new_row, new_col)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands
