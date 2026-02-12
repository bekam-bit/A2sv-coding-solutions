class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])

        zero_rows=set()
        zero_cols=set()

        for r_idx in range(rows):
            for c_idx in range(cols):
                if matrix[r_idx][c_idx] == 0:
                    zero_rows.add(r_idx)
                    zero_cols.add(c_idx)
        
        for r_idx in range(rows):
            for c_idx in range(cols):
                if (r_idx in zero_rows or c_idx in zero_cols) and matrix[r_idx][c_idx] != 0:
                    matrix[r_idx][c_idx] = 0
