class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])
        
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        pacific_reachable = set()
        atlantic_reachable = set()

        def inbound(row, col):
            return (0 <= row < rows and 0 <= col < cols)
        
        def dfs(row, col, reachable):
            reachable.add((row, col))
            
            for dr, dc in dir:
                new_row, new_col = row + dr, col + dc
                
                if inbound(new_row, new_col) and (new_row, new_col) not in reachable and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, reachable)
        
        for r in range(rows):
            dfs(r, 0, pacific_reachable)
        for c in range(cols):
            dfs(0, c, pacific_reachable)
        
        for r in range(rows):
            dfs(r, cols - 1, atlantic_reachable)
        for c in range(cols):
            dfs(rows - 1, c, atlantic_reachable)
        
        return [list(cell) for cell in (pacific_reachable & atlantic_reachable)]