from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        
        if k == 0:
            return grid
        
        result = [[0] * n for _ in range(m)]
        
        for old_1d in range(total):
            new_1d = (old_1d + k) % total
            
            old_r, old_c = old_1d // n, old_1d % n
            
            new_r, new_c = new_1d // n, new_1d % n
            
            result[new_r][new_c] = grid[old_r][old_c]
            
        return result