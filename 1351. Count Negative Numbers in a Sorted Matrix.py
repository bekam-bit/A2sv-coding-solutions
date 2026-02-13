class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        total_cnt=0
        
        for row in range(row_len):
            left=0
            right=col_len - 1
            first_neg=col_len

            while left <= right:

                mid_col=(left + right)//2

                if self.isNegative(grid[row][mid_col]):
                    first_neg=mid_col
                    right = mid_col - 1

                else:
                    left = mid_col + 1

            total_cnt += col_len - first_neg

        return total_cnt
    
    def isNegative(self,num):
        return True if num < 0 else False
