class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        cols=len(matrix[0])

        res=[[0] * rows for _ in range(cols)]

        for row_idx in range(rows):
            for col_idx in range(cols):
                res[col_idx][row_idx] = matrix[row_idx][col_idx]
        
        return res
