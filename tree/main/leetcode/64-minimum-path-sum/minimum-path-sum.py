class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        dp[m - 1][n - 1] = grid[m - 1][n - 1]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue
                    
                if c + 1 < n:
                    right = grid[r][c] + dp[r][c + 1]
                else:
                    right = float('inf')

                if r + 1 < m:
                    down = grid[r][c] + dp[r + 1][c]
                else:
                    down = float('inf')

                dp[r][c] = min(right, down)
        
        return dp[0][0]